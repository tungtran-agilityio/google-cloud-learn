#!/usr/bin/env python3
"""
Simple example for the Text Processing Cloud Function
"""

import requests
import json
import os


def test_simple_function(function_url):
    """Test the simple Cloud Function"""
    print("🚀 Simple Cloud Function Test")
    print("=" * 40)
    
    # Test 1: GET request
    print("\n1. GET Request Test")
    try:
        response = requests.get(f"{function_url}?text=Hello World")
        if response.status_code == 200:
            data = response.json()
            print("✅ GET request successful")
            print(f"   Original: {data['original_text']}")
            print(f"   Characters: {data['character_count']}")
            print(f"   Words: {data['word_count']}")
            print(f"   Uppercase: {data['uppercase']}")
            print(f"   Lowercase: {data['lowercase']}")
            print(f"   Reversed: {data['reversed']}")
        else:
            print(f"❌ GET request failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: POST request
    print("\n2. POST Request Test")
    try:
        data = {"text": "Cloud Function Test"}
        response = requests.post(function_url, json=data)
        if response.status_code == 200:
            result = response.json()
            print("✅ POST request successful")
            print(f"   Message: {result['message']}")
            print(f"   Word count: {result['word_count']}")
        else:
            print(f"❌ POST request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Error handling
    print("\n3. Error Handling Test")
    try:
        response = requests.get(function_url)  # No text parameter
        if response.status_code == 400:
            data = response.json()
            print("✅ Error handling works correctly")
            print(f"   Error: {data['error']}")
        else:
            print(f"❌ Expected error but got: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 4: Different text inputs
    print("\n4. Different Text Inputs")
    test_texts = [
        "Simple text",
        "This is a longer sentence with more words.",
        "123 numbers and symbols!@#",
        "Mixed CASE text"
    ]
    
    for text in test_texts:
        try:
            response = requests.get(f"{function_url}?text={text}")
            if response.status_code == 200:
                data = response.json()
                print(f"   '{text}' -> {data['word_count']} words, {data['character_count']} chars")
            else:
                print(f"   '{text}' -> Error: {response.status_code}")
        except Exception as e:
            print(f"   '{text}' -> Exception: {e}")
    
    print("\n🎉 All tests completed!")


def main():
    """Main function"""
    # Get function URL from environment or use default
    function_url = os.environ.get('FUNCTION_URL', 'https://simple-text-function-bdxvjrgija-uc.a.run.app')
    
    print(f"Testing Cloud Function at: {function_url}")
    print("Note: Make sure the function is deployed or running locally")
    print()
    
    test_simple_function(function_url)


if __name__ == "__main__":
    main()