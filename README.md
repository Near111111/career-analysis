# 🎯 Career Analysis - AI-Powered Career Recommendation System

An intelligent career recommendation system that uses Machine Learning (Random Forest) to predict the top 5 best-matching careers based on a 12-question personality and interest assessment.

## 📋 Features

- ✅ **130+ Career Options** across 14 different categories
- ✅ **Machine Learning Powered** using Random Forest Classifier
- ✅ **70-85% Accuracy** in career predictions
- ✅ **Top 5 Recommendations** with match percentages
- ✅ **Interactive Survey** with easy-to-use command-line interface
- ✅ **Synthetic Dataset Generator** for training data

## 🗂️ Project Structure

```
CareerAnalysis/
├── career_dataset.csv              # Training dataset (auto-generated)
├── train_model.py                  # Model training script
├── career_predictor.py             # Prediction module
├── test_survey.py                  # Interactive survey test
├── generate_dataset/
│   └── GenerateCareerDataSet.py    # Dataset generator
├── model/                          # Model files (generated, not in git)
│   ├── career_model.pkl           # Trained model
│   └── model_metadata.pkl         # Model information
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Near111111/career-analysis.git
   cd career-analysis
   ```

2. **Install required packages**

   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```

3. **Generate the training dataset**

   ```bash
   python generate_dataset/GenerateCareerDataSet.py
   ```

   This creates `career_dataset.csv` with ~6,500 training samples across 130+ careers.

4. **Train the model**

   ```bash
   python train_model.py
   ```

   This creates the `model/` folder with trained model files (~210 MB).

5. **Test the system**
   ```bash
   python test_survey.py
   ```
   Answer 12 questions and get your top 5 career recommendations!

## 📊 Career Categories

The system covers 130+ careers across these categories:

1. **Information Technology & Computer Science** (12 careers)
2. **Business & Management** (11 careers)
3. **Engineering & Architecture** (9 careers)
4. **Healthcare & Medical** (10 careers)
5. **Education & Training** (6 careers)
6. **Arts, Design & Media** (12 careers)
7. **Trades & Technical Work** (7 careers)
8. **Law, Government & Public Safety** (8 careers)
9. **Finance & Economics** (6 careers)
10. **Science & Research** (7 careers)
11. **Hospitality & Tourism** (6 careers)
12. **Agriculture & Environment** (5 careers)
13. **Logistics & Transportation** (6 careers)
14. **Others** (6 careers)

## 🧪 How It Works

### The 12 Assessment Questions

The system evaluates users based on these dimensions:

1. **Q1:** Math & Problem Solving aptitude
2. **Q2:** Tech savviness
3. **Q3:** Preference for computer work vs physical work
4. **Q4:** Creativity level
5. **Q5:** Social & people skills
6. **Q6:** Detail-orientation
7. **Q7:** Interest in research & analysis
8. **Q8:** Comfort with fast-paced environments
9. **Q9:** Teaching & mentoring ability
10. **Q10:** Interest in outdoor/field work
11. **Q11:** Technical & hands-on skills
12. **Q12:** Business & entrepreneurship interest

Each question is rated on a scale of 1-5:

- **1** = Very Low / Not at all
- **2** = Low / Slightly
- **3** = Neutral / Moderate
- **4** = High / Considerably
- **5** = Very High / Extremely

### Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Trees:** 200 estimators
- **Training Data:** 6,500+ synthetic samples
- **Accuracy:** 70-85% on test set
- **Output:** Top 5 career predictions with match percentages

## 💻 Usage

### As a Python Module

```python
from career_predictor import CareerPredictor

# Initialize predictor
predictor = CareerPredictor()

# User answers (Q1-Q12, values 1-5)
answers = [5, 5, 5, 3, 2, 4, 4, 4, 2, 1, 4, 3]

# Get top 5 predictions
results = predictor.predict_top5(answers)

# Output format:
# [
#     {'rank': 1, 'career': 'Software Developer', 'percentage': 45.32},
#     {'rank': 2, 'career': 'Data Scientist', 'percentage': 28.15},
#     {'rank': 3, 'career': 'Web Developer', 'percentage': 12.48},
#     {'rank': 4, 'career': 'Game Developer', 'percentage': 8.21},
#     {'rank': 5, 'career': 'Mobile App Developer', 'percentage': 5.84}
# ]
```

### Interactive Survey

```bash
python test_survey.py
```

Sample output:

```
🎯 YOUR TOP 5 RECOMMENDED CAREERS
====================================================================

🥇 RANK 1: Software Developer
   Match Score: 45.32%
   [████████████████████░░░░░░░░░░░░░░░░░░░░]

🥈 RANK 2: Data Scientist
   Match Score: 28.15%
   [███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]
```

## 🔧 Adding New Careers

1. **Edit `generate_dataset/GenerateCareerDataSet.py`**

   Add your career to the appropriate category:

   ```python
   careers = {
       "IT & Computer Science": [
           "Software Developer",
           "Your New Career",  # Add here
           # ...
       ]
   }
   ```

2. **Define the career pattern**

   Create a typical answer pattern (Q1-Q12):

   ```python
   career_patterns = {
       "Your New Career": [5, 5, 5, 3, 2, 4, 4, 4, 2, 1, 4, 3],
       # Values represent typical answers for Q1-Q12
   }
   ```

3. **Regenerate dataset and retrain**
   ```bash
   python generate_dataset/GenerateCareerDataSet.py
   python train_model.py
   ```

## 📈 Model Performance

- **Decision Tree (single):** ~44-50% accuracy
- **Random Forest (200 trees):** ~70-85% accuracy
- **Training time:** ~30-60 seconds
- **Prediction time:** <1 second

## 🤝 Future Enhancements

- [ ] Web interface (Flask/Django)
- [ ] REST API endpoints
- [ ] Database integration
- [ ] User authentication
- [ ] Career details and job descriptions
- [ ] Save and compare results
- [ ] Mobile app version

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Near111111**

- GitHub: [@Near111111](https://github.com/Near111111)

## 🙏 Acknowledgments

- Built with scikit-learn
- Inspired by career aptitude assessments
- Synthetic data generation for ML training

---

⭐ **Star this repo** if you find it helpful!

📧 **Questions?** Open an issue or reach out!
