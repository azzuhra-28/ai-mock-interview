"""
Data Loader Module
Handles loading and validation of external datasets
"""

import json
from pathlib import Path


class DataLoader:
    """
    Loads datasets from external files
    """
    
    def __init__(self, data_dir='data'):
        """
        Initialize data loader
        
        Args:
            data_dir (str): Directory containing data files
        """
        self.data_dir = Path(data_dir)
        
        # Ensure data directory exists
        if not self.data_dir.exists():
            self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def load_questions(self):
        """
        Load interview questions from JSON file
        
        Returns:
            dict: Questions organized by category
        """
        filepath = self.data_dir / 'questions.json'
        
        if not filepath.exists():
            # Return default questions if file doesn't exist
            return self._get_default_questions()
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading questions: {e}")
            return self._get_default_questions()
    
    def load_keywords(self):
        """
        Load category-specific keywords
        
        Returns:
            dict: Keywords by category
        """
        filepath = self.data_dir / 'keywords.json'
        
        if not filepath.exists():
            return self._get_default_keywords()
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading keywords: {e}")
            return self._get_default_keywords()
    
    def load_best_answers(self):
        """
        Load sample best practice answers
        
        Returns:
            dict: Best answers by category
        """
        filepath = self.data_dir / 'best_answers.json'
        
        if not filepath.exists():
            return self._get_default_best_answers()
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading best answers: {e}")
            return self._get_default_best_answers()
    
    def load_stopwords(self):
        """
        Load stopwords for text preprocessing from files or use defaults
        Supports both Indonesian and English stopwords
        
        Returns:
            set: Combined set of stopwords (Indonesian + English)
        """
        stopwords = set()
        
        # Try to load Indonesian stopwords
        id_filepath = self.data_dir / 'stopwords_id.txt'
        if id_filepath.exists():
            try:
                with open(id_filepath, 'r', encoding='utf-8') as f:
                    id_words = set(line.strip().lower() for line in f if line.strip())
                stopwords.update(id_words)
                print(f"✅ Loaded {len(id_words)} Indonesian stopwords from file")
            except Exception as e:
                print(f"⚠️ Error loading Indonesian stopwords: {e}")
        else:
            # Fallback: Comprehensive Indonesian stopwords
            default_id = {
                'yang', 'untuk', 'pada', 'ke', 'para', 'namun', 'menurut', 'antara',
                'dia', 'dua', 'ia', 'seperti', 'jika', 'sehingga', 'kembali', 'dengan',
                'dan', 'di', 'dari', 'ini', 'itu', 'tidak', 'ada', 'atau', 'oleh',
                'sebagai', 'adalah', 'akan', 'saya', 'kami', 'kita', 'mereka', 'anda',
                'juga', 'sudah', 'dapat', 'telah', 'bisa', 'sangat', 'hanya', 'dalam',
                'tersebut', 'hal', 'masih', 'saat', 'bahwa', 'karena', 'ketika', 'setelah',
                'selama', 'hingga', 'serta', 'maka', 'masing', 'sama', 'lain', 'lebih',
                'pernah', 'belum', 'banyak', 'antara', 'sekitar', 'sekali', 'setiap',
                'semua', 'sebuah', 'suatu', 'bila', 'apabila', 'bahwa', 'dimana',
                'dimana', 'kepada', 'terhadap', 'yaitu', 'yakni'
            }
            stopwords.update(default_id)
            print(f"⚠️ File not found, using {len(default_id)} default Indonesian stopwords")
        
        # Try to load English stopwords
        en_filepath = self.data_dir / 'stopwords_english.txt'
        if en_filepath.exists():
            try:
                with open(en_filepath, 'r', encoding='utf-8') as f:
                    en_words = set(line.strip().lower() for line in f if line.strip())
                stopwords.update(en_words)
                print(f"✅ Loaded {len(en_words)} English stopwords from file")
            except Exception as e:
                print(f"⚠️ Error loading English stopwords: {e}")
        else:
            # Fallback: Essential English stopwords
            default_en = {
                'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
                'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
                'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
                'who', 'when', 'where', 'why', 'how', 'if', 'then', 'than', 'so',
                'just', 'only', 'very', 'too', 'also', 'about', 'into', 'through',
                'over', 'before', 'after', 'above', 'below', 'between', 'under',
                'again', 'once', 'here', 'there', 'all', 'both', 'each', 'few',
                'more', 'most', 'some', 'such', 'no', 'not', 'yes', 'other', 'any'
            }
            stopwords.update(default_en)
            print(f"⚠️ File not found, using {len(default_en)} default English stopwords")
    
        print(f"📊 Total stopwords loaded: {len(stopwords)}")
        return stopwords
    
    def save_questions(self, questions):
        """Save questions to JSON file"""
        filepath = self.data_dir / 'questions.json'
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
    
    def save_keywords(self, keywords):
        """Save keywords to JSON file"""
        filepath = self.data_dir / 'keywords.json'
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(keywords, f, indent=2, ensure_ascii=False)
    
    def save_best_answers(self, answers):
        """Save best answers to JSON file"""
        filepath = self.data_dir / 'best_answers.json'
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(answers, f, indent=2, ensure_ascii=False)
    
    def _get_default_questions(self):
        """Return default question set"""
        return {
            "Technical Skills & Background": {
                "question": "Jelaskan pengalaman Anda dalam menggunakan Python dan library data science (pandas, numpy, scikit-learn). Berikan contoh project spesifik.",
                "keywords": ["python", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "data", "model", "project", "experience"],
                "ideal_length": (100, 250),
                "weight": {"technical": 0.4, "depth": 0.3, "structure": 0.3}
            },
            "Statistical Knowledge": {
                "question": "Bagaimana Anda menjelaskan perbedaan antara supervised dan unsupervised learning kepada non-technical stakeholder? Berikan contoh use case masing-masing.",
                "keywords": ["supervised", "unsupervised", "machine learning", "classification", "regression", "clustering", "model", "prediction", "example", "use case"],
                "ideal_length": (80, 200),
                "weight": {"technical": 0.3, "depth": 0.3, "structure": 0.4}
            },
            "Data Wrangling & EDA": {
                "question": "Ceritakan pengalaman Anda dalam melakukan data cleaning dan exploratory data analysis. Apa challenges terbesar yang Anda hadapi?",
                "keywords": ["cleaning", "missing values", "outliers", "visualization", "eda", "exploratory", "data quality", "preprocessing", "challenge", "solution"],
                "ideal_length": (100, 250),
                "weight": {"technical": 0.35, "depth": 0.35, "structure": 0.3}
            },
            "Problem Solving & Case Study": {
                "question": "Bayangkan Anda diminta untuk membuat model prediksi churn customer. Jelaskan langkah-langkah yang akan Anda ambil dari awal hingga deployment.",
                "keywords": ["churn", "prediction", "model", "feature engineering", "evaluation", "metrics", "deployment", "business impact", "step", "process"],
                "ideal_length": (150, 300),
                "weight": {"technical": 0.3, "depth": 0.4, "structure": 0.3}
            },
            "Business Acumen": {
                "question": "Bagaimana Anda memastikan bahwa model machine learning yang Anda buat memberikan value kepada bisnis? Berikan contoh metrik yang Anda gunakan.",
                "keywords": ["business value", "roi", "impact", "metrics", "kpi", "stakeholder", "decision", "actionable", "example", "measurement"],
                "ideal_length": (80, 200),
                "weight": {"technical": 0.25, "depth": 0.35, "structure": 0.4}
            },
            "Communication & Collaboration": {
                "question": "Jelaskan pengalaman Anda dalam berkomunikasi hasil analisis data kepada tim non-technical. Bagaimana Anda menyederhanakan konsep kompleks?",
                "keywords": ["communication", "visualization", "presentation", "stakeholder", "explain", "simple", "storytelling", "dashboard", "non-technical", "audience"],
                "ideal_length": (80, 200),
                "weight": {"technical": 0.2, "depth": 0.3, "structure": 0.5}
            }
        }
    
    def _get_default_keywords(self):
        """Return default category keywords"""
        return {
            "Technical Skills & Background": [
                "experience", "project", "implementation", "result", "technology", 
                "framework", "library", "development", "coding", "programming"
            ],
            "Statistical Knowledge": [
                "concept", "difference", "example", "application", "scenario", 
                "business", "supervised", "unsupervised", "algorithm", "method"
            ],
            "Data Wrangling & EDA": [
                "process", "approach", "tool", "challenge", "solution", "insight",
                "analysis", "visualization", "pattern", "quality"
            ],
            "Problem Solving & Case Study": [
                "step", "methodology", "analysis", "testing", "deployment", 
                "monitoring", "evaluation", "optimization", "iteration", "validation"
            ],
            "Business Acumen": [
                "impact", "metric", "value", "stakeholder", "decision", "outcome",
                "roi", "kpi", "business", "strategy"
            ],
            "Communication & Collaboration": [
                "audience", "simplify", "visual", "feedback", "collaboration", 
                "understanding", "presentation", "storytelling", "explain", "clarity"
            ]
        }
    
    def _get_default_best_answers(self):
        """Return default best practice answers"""
        return {
            "Technical Skills & Background": {
                "answer": """I have extensive experience with Python and its data science ecosystem. In my recent project predicting customer lifetime value, I used pandas for data manipulation, handling 2M+ customer records. I implemented feature engineering using numpy arrays for computational efficiency. For modeling, I utilized scikit-learn's ensemble methods, specifically RandomForestRegressor and GradientBoostingRegressor, achieving 85% accuracy. The project involved building a complete pipeline from data ingestion to model deployment using Docker containers. I also experimented with TensorFlow for deep learning approaches to compare performance."""
            },
            "Statistical Knowledge": {
                "answer": """To explain supervised vs unsupervised learning to non-technical stakeholders, I use practical analogies. Supervised learning is like teaching a child with flashcards - you show examples with correct answers. For instance, email spam detection where we train the model with labeled emails. Unsupervised learning is like organizing a messy room without instructions - the model finds patterns on its own. Customer segmentation is a great example, where we group customers by behavior without predefined categories. The key difference is whether we provide the 'answers' during training."""
            },
            "Data Wrangling & EDA": {
                "answer": """In a recent healthcare analytics project, I faced significant data quality challenges. The dataset had 30% missing values across critical features. I implemented multiple imputation strategies - mean/median for numerical data, mode for categorical, and KNN imputation for complex patterns. For outliers, I used IQR method and domain knowledge to distinguish genuine anomalies from data errors. My EDA revealed unexpected correlations through correlation matrices and revealed seasonality patterns via time series decomposition. The biggest challenge was handling inconsistent data formats across different source systems, which I resolved through extensive data profiling and standardization."""
            }
        }
