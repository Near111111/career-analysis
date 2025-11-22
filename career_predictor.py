import pickle
import numpy as np
import os

class CareerPredictor:
    """
    Career Prediction Model
    
    Usage:
        predictor = CareerPredictor()
        results = predictor.predict_top5([5, 5, 5, 3, 2, 4, 4, 4, 2, 1, 4, 3])
    """
    
    def __init__(self, model_path="model/career_model.pkl"):
        """Load the trained model"""
        self.model_path = model_path
        self.model = None
        self.metadata = None
        self.load_model()
    
    def load_model(self):
        """Load the saved model from disk"""
        try:
            # Load model
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            
            # Load metadata
            metadata_path = self.model_path.replace('career_model.pkl', 'model_metadata.pkl')
            if os.path.exists(metadata_path):
                with open(metadata_path, 'rb') as f:
                    self.metadata = pickle.load(f)
            
            print(f"✓ Model loaded successfully from {self.model_path}")
            if self.metadata:
                print(f"✓ Model accuracy: {self.metadata['accuracy']*100:.2f}%")
        
        except Exception as e:
            raise Exception(f"Error loading model: {e}")
    
    def predict_top5(self, answers):
        """
        Predict top 5 careers based on user answers
        
        Args:
            answers: List of 12 integers (1-5) representing Q1-Q12
            
        Returns:
            List of dictionaries with career and percentage
            [
                {'rank': 1, 'career': 'Software Developer', 'percentage': 45.32},
                {'rank': 2, 'career': 'Data Scientist', 'percentage': 28.15},
                ...
            ]
        """
        # Validate input
        if len(answers) != 12:
            raise ValueError("Expected 12 answers (Q1-Q12)")
        
        if not all(1 <= ans <= 5 for ans in answers):
            raise ValueError("All answers must be between 1 and 5")
        
        # Prepare input
        user_input = np.array(answers).reshape(1, -1)
        
        # Get probabilities for all careers
        probabilities = self.model.predict_proba(user_input)[0]
        
        # Get top 5 indices
        top5_indices = np.argsort(probabilities)[-5:][::-1]
        
        # Build results
        results = []
        for i, idx in enumerate(top5_indices):
            career = self.model.classes_[idx]
            percentage = probabilities[idx] * 100
            
            results.append({
                'rank': i + 1,
                'career': career,
                'percentage': round(percentage, 2)
            })
        
        return results
    
    def predict_single(self, answers):
        """
        Predict single best career
        
        Args:
            answers: List of 12 integers (1-5)
            
        Returns:
            String - predicted career name
        """
        user_input = np.array(answers).reshape(1, -1)
        prediction = self.model.predict(user_input)[0]
        return prediction
    
    def get_model_info(self):
        """Get model information"""
        if self.metadata:
            return {
                'accuracy': f"{self.metadata['accuracy']*100:.2f}%",
                'total_careers': self.metadata['n_careers'],
                'model_type': self.metadata['model_type'],
                'n_estimators': self.metadata.get('n_estimators', 'N/A')
            }
        return {'status': 'No metadata available'}


# Example usage and testing
if __name__ == "__main__":
    print("=" * 60)
    print("CAREER PREDICTOR MODULE TEST")
    print("=" * 60)
    
    # Initialize predictor
    predictor = CareerPredictor()
    
    # Show model info
    print("\n📊 Model Information:")
    info = predictor.get_model_info()
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    # Test with sample answers
    print("\n🧪 Testing with sample answers...")
    sample_answers = [5, 5, 5, 3, 2, 4, 4, 4, 2, 1, 4, 3]
    print(f"   Answers: {sample_answers}")
    
    # Get top 5 predictions
    print("\n🎯 TOP 5 CAREER PREDICTIONS:")
    print("-" * 60)
    
    results = predictor.predict_top5(sample_answers)
    
    medals = ["🥇", "🥈", "🥉", "🏅", "⭐"]
    
    for result in results:
        rank = result['rank']
        career = result['career']
        percentage = result['percentage']
        medal = medals[rank-1]
        
        # Progress bar
        bar_length = 30
        filled = int(bar_length * percentage / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        print(f"\n{medal} RANK {rank}: {career}")
        print(f"   Match Score: {percentage:.2f}%")
        print(f"   [{bar}]")
    
    print("\n" + "=" * 60)
    print("✨ TEST COMPLETE!")
    print("=" * 60)