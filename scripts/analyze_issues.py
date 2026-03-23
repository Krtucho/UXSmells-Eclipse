import csv
from collections import Counter
import re
import os

def analyze():
    filepath = os.path.join(os.path.dirname(__file__), "..", "results", "eclipse_ux_issues.csv")
    titles = []
    all_labels = []
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                titles.append(row["Title"])
                if row["Labels"]:
                    all_labels.extend([l.strip() for l in row["Labels"].split(",")])
                    
        label_counts = Counter(all_labels)
        
        stopwords = set(["the", "a", "to", "in", "of", "and", "is", "for", "on", "with", "not", "when", "by", "as", "at", "it", "from", "be", "an", "are", "this", "that", "which", "or", "but", "if", "has", "have", "can", "should", "do", "does", "doesnt", "dont", "eclipse", "ui", "ux", "issue", "bug"])
        words = []
        for title in titles:
            tokens = re.findall(r'\b[a-zA-Z]{3,}\b', title.lower())
            words.extend([w for w in tokens if w not in stopwords])
            
        word_counts = Counter(words)
        
        print("TOP 10 LABELS:")
        for label, count in label_counts.most_common(10):
            print(f"- {label}: {count}")
            
        print("\nTOP 20 WORDS IN TITLES:")
        for word, count in word_counts.most_common(20):
            print(f"- {word}: {count}")
            
    except Exception as e:
        print(f"Error analyzing: {e}")

if __name__ == "__main__":
    analyze()
