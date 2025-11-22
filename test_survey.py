from career_predictor import CareerPredictor
import sys

# Survey Questions
questions = [
    "Gaano ka kahilig sa Math at Problem Solving?",
    "Gaano ka ka-tech savvy?",
    "Gusto mo ba magtrabaho sa computer kaysa physical work?",
    "Gaano ka ka-creative (design, art, content creation)?",
    "Gaano mo gusto ang pakikipag-socialize / pag-handle ng tao?",
    "Gaano ka ka-detail-oriented?",
    "Gusto mo ba research, analysis, or investigation type work?",
    "Gaano ka ka-comfortable sa fast-paced environments?",
    "Mahilig ka ba magturo, magpaliwanag, or mag-guide ng ibang tao?",
    "Gusto mo ba outdoor or field work kaysa office work?",
    "Interested ka ba sa technical/hands-on tasks?",
    "Gaano ka ka-interesado sa business, finance, or entrepreneurship?"
]

def print_header():
    """Print welcome header"""
    print("\n" + "=" * 70)
    print("🎯 CAREER RECOMMENDATION SYSTEM - SURVEY TEST")
    print("=" * 70)
    print("\n📋 Instructions:")
    print("   - Answer each question with a number from 1 to 5")
    print("   - 1 = Hindi/Very Low")
    print("   - 2 = Medyo/Low")
    print("   - 3 = Katamtaman/Neutral")
    print("   - 4 = Oo/High")
    print("   - 5 = Sobra/Very High")
    print("\n" + "=" * 70)

def get_user_answers():
    """Get answers from user"""
    answers = []
    
    print("\n🔹 SAGUTAN ANG SURVEY:\n")
    
    for i, question in enumerate(questions, 1):
        while True:
            try:
                print(f"Q{i}. {question}")
                answer = int(input(f"    Your answer (1-5): "))
                
                if 1 <= answer <= 5:
                    answers.append(answer)
                    print("    ✓ Saved!\n")
                    break
                else:
                    print("    ⚠️  Please enter a number between 1 and 5!\n")
            except ValueError:
                print("    ⚠️  Invalid input! Please enter a number.\n")
            except KeyboardInterrupt:
                print("\n\n❌ Survey cancelled by user.")
                sys.exit(0)
    
    return answers

def display_results(results):
    """Display prediction results"""
    print("\n" + "=" * 70)
    print("🎯 YOUR TOP 5 RECOMMENDED CAREERS")
    print("=" * 70)
    
    medals = ["🥇", "🥈", "🥉", "🏅", "⭐"]
    
    for result in results:
        rank = result['rank']
        career = result['career']
        percentage = result['percentage']
        medal = medals[rank - 1]
        
        # Create progress bar
        bar_length = 40
        filled = int(bar_length * percentage / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        print(f"\n{medal} RANK {rank}: {career}")
        print(f"   Match Score: {percentage:.2f}%")
        print(f"   [{bar}]")
    
    print("\n" + "=" * 70)

def main():
    """Main function"""
    print_header()
    
    # Initialize predictor
    try:
        print("\n🔄 Loading prediction model...")
        predictor = CareerPredictor()
        print("✓ Model loaded successfully!\n")
    except Exception as e:
        print(f"\n❌ ERROR: Failed to load model!")
        print(f"   {e}")
        print("\n💡 Make sure you've run 'train_model.py' first!")
        sys.exit(1)
    
    # Show model info
    print("📊 Model Information:")
    info = predictor.get_model_info()
    for key, value in info.items():
        print(f"   • {key}: {value}")
    
    # Get user answers
    try:
        answers = get_user_answers()
    except Exception as e:
        print(f"\n❌ Error getting answers: {e}")
        sys.exit(1)
    
    # Show user's answers
    print("\n📝 Your Answers:")
    print(f"   {answers}")
    
    # Make prediction
    print("\n🔍 Analyzing your answers...")
    try:
        results = predictor.predict_top5(answers)
    except Exception as e:
        print(f"\n❌ Prediction error: {e}")
        sys.exit(1)
    
    # Display results
    display_results(results)
    
    # Ask if user wants to try again
    print("\n💡 Tips:")
    print("   • Your top match is the career that best fits your profile")
    print("   • Consider exploring careers in your top 3 results")
    print("   • Higher percentages indicate stronger matches")
    
    print("\n" + "=" * 70)
    
    try_again = input("\n🔄 Want to try again with different answers? (y/n): ").lower()
    if try_again == 'y':
        main()
    else:
        print("\n✨ Thank you for using the Career Recommendation System!")
        print("=" * 70 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)