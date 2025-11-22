from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from career_predictor import CareerPredictor
import os
import subprocess

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize predictor once when server starts
def initialize_model():
    """Initialize the model, train if not exists"""
    # Check if model exists
    if not os.path.exists('model/career_model.pkl'):
        print("⚠️  Model not found! Training new model...")
        print("⏳ This may take 30-60 seconds...")
        
        try:
            result = subprocess.run(['python', 'train_model.py'], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Model trained successfully!")
            else:
                print(f"❌ Training failed: {result.stderr}")
                return None
        except Exception as e:
            print(f"❌ Error training model: {e}")
            return None
    
    # Load the model
    try:
        predictor = CareerPredictor()
        print("✅ Model loaded successfully!")
        return predictor
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None

predictor = initialize_model()

# Questions for the survey
QUESTIONS = [
    {
        "id": 1,
        "question": "Gaano ka kahilig sa Math at Problem Solving?",
        "description": "Problem-solving skills and mathematical aptitude"
    },
    {
        "id": 2,
        "question": "Gaano ka ka-tech savvy?",
        "description": "Comfort with technology and digital tools"
    },
    {
        "id": 3,
        "question": "Gusto mo ba magtrabaho sa computer kaysa physical work?",
        "description": "Preference for computer-based vs hands-on work"
    },
    {
        "id": 4,
        "question": "Gaano ka ka-creative (design, art, content creation)?",
        "description": "Creative and artistic abilities"
    },
    {
        "id": 5,
        "question": "Gaano mo gusto ang pakikipag-socialize / pag-handle ng tao?",
        "description": "Social and people management skills"
    },
    {
        "id": 6,
        "question": "Gaano ka ka-detail-oriented?",
        "description": "Attention to detail and precision"
    },
    {
        "id": 7,
        "question": "Gusto mo ba research, analysis, or investigation type work?",
        "description": "Interest in research and analytical work"
    },
    {
        "id": 8,
        "question": "Gaano ka ka-comfortable sa fast-paced environments?",
        "description": "Ability to thrive in dynamic settings"
    },
    {
        "id": 9,
        "question": "Mahilig ka ba magturo, magpaliwanag, or mag-guide ng ibang tao?",
        "description": "Teaching and mentoring abilities"
    },
    {
        "id": 10,
        "question": "Gusto mo ba outdoor or field work kaysa office work?",
        "description": "Preference for outdoor vs indoor work"
    },
    {
        "id": 11,
        "question": "Interested ka ba sa technical/hands-on tasks?",
        "description": "Technical and practical skills"
    },
    {
        "id": 12,
        "question": "Gaano ka ka-interesado sa business, finance, or entrepreneurship?",
        "description": "Business and financial interests"
    }
]

@app.route('/')
def home():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    """Return all survey questions"""
    return jsonify({
        'success': True,
        'questions': QUESTIONS
    })

@app.route('/api/predict', methods=['POST'])
def predict_career():
    """
    Predict careers based on user answers
    
    Expected JSON:
    {
        "answers": [5, 5, 5, 3, 2, 4, 4, 4, 2, 1, 4, 3]
    }
    
    Returns:
    {
        "success": true,
        "predictions": [
            {"rank": 1, "career": "Software Developer", "percentage": 45.32},
            ...
        ]
    }
    """
    try:
        if not predictor:
            return jsonify({
                'success': False,
                'error': 'Model not loaded. Please train the model first.'
            }), 500
        
        # Get answers from request
        data = request.get_json()
        
        if not data or 'answers' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing "answers" in request body'
            }), 400
        
        answers = data['answers']
        
        # Validate answers
        if len(answers) != 12:
            return jsonify({
                'success': False,
                'error': 'Expected 12 answers'
            }), 400
        
        if not all(isinstance(ans, int) and 1 <= ans <= 5 for ans in answers):
            return jsonify({
                'success': False,
                'error': 'All answers must be integers between 1 and 5'
            }), 400
        
        # Get predictions
        predictions = predictor.predict_top5(answers)
        
        # Get model info
        model_info = predictor.get_model_info()
        
        return jsonify({
            'success': True,
            'predictions': predictions,
            'model_info': model_info,
            'answers': answers
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/model-info', methods=['GET'])
def get_model_info():
    """Get model information"""
    try:
        if not predictor:
            return jsonify({
                'success': False,
                'error': 'Model not loaded'
            }), 500
        
        info = predictor.get_model_info()
        return jsonify({
            'success': True,
            'model_info': info
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': predictor is not None
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 CAREER ANALYSIS - Flask Server")
    print("="*60)
    print(f"📊 Model Status: {'✓ Loaded' if predictor else '✗ Not Loaded'}")
    
    if not predictor:
        print("⚠️  WARNING: Model not loaded. Server may not work properly.")
    
    # Get port from environment variable (for deployment)
    port = int(os.environ.get('PORT', 5000))
    
    print(f"🌐 Server running on: http://0.0.0.0:{port}")
    print("📋 API Endpoints:")
    print("   GET  /                 - Main page")
    print("   GET  /api/questions    - Get survey questions")
    print("   POST /api/predict      - Get career predictions")
    print("   GET  /api/model-info   - Get model information")
    print("   GET  /health           - Health check")
    print("="*60 + "\n")
    
    # Production vs Development
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)