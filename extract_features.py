import re

def get_url_length(url):
    return len(url)

def has_ip_address(url):
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    return 1 if re.search(ip_pattern, url) else 0

def is_https(url):
    return 1 if url.startswith("https") else 0

def has_suspicious_words(url):
    suspicious_words = ['free', 'win', 'bonus', 'offer', 'login', 'verify']
    return 1 if any(word in url.lower() for word in suspicious_words) else 0

def count_dots(url):
    return url.count('.')

def count_hyphens(url):
    return url.count('-')

def extract_all_features(url):
    return {
        "url_length": get_url_length(url),
        "has_ip": has_ip_address(url),
        "is_https": is_https(url),
        "suspicious_words": has_suspicious_words(url),
        "dot_count": count_dots(url),
        "hyphen_count": count_hyphens(url)
    }