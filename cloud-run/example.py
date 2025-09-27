#!/usr/bin/env python3
"""
Example usage script for the Simple Demo API
This script demonstrates all the available endpoints
"""

import requests
import json
import os


def test_api(base_url):
    """Test all API endpoints"""
    print("🚀 Simple Demo API Test")
    print("=" * 40)
    
    # Test home endpoint
    print("\n1. API Information")
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            print("✅ API Info retrieved")
            print(f"   Service: {data['message']}")
            print(f"   Version: {data['version']}")
            print(f"   Description: {data['description']}")
        else:
            print(f"❌ Failed to get API info: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test health endpoint
    print("\n2. Health Check")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print("✅ Service is healthy")
            print(f"   Status: {data['status']}")
            print(f"   Service: {data['service']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test time endpoint
    print("\n3. Current Time")
    try:
        response = requests.get(f"{base_url}/time")
        if response.status_code == 200:
            data = response.json()
            print("✅ Time retrieved")
            print(f"   Current Time: {data['current_time']}")
            print(f"   Formatted: {data['formatted']}")
        else:
            print(f"❌ Time request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test random number generator
    print("\n4. Random Numbers")
    try:
        response = requests.get(f"{base_url}/random?min=1&max=50&count=5")
        if response.status_code == 200:
            data = response.json()
            print("✅ Random numbers generated")
            print(f"   Numbers: {data['numbers']}")
            print(f"   Sum: {data['sum']}")
            print(f"   Average: {data['average']}")
        else:
            print(f"❌ Random request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test quote endpoint
    print("\n5. Inspirational Quote")
    try:
        response = requests.get(f"{base_url}/quote")
        if response.status_code == 200:
            data = response.json()
            print("✅ Quote retrieved")
            print(f"   Quote: {data['quote']}")
        else:
            print(f"❌ Quote request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test fake weather
    print("\n6. Fake Weather Data")
    try:
        response = requests.get(f"{base_url}/weather/London")
        if response.status_code == 200:
            data = response.json()
            print("✅ Weather data retrieved")
            print(f"   City: {data['city']}")
            print(f"   Temperature: {data['temperature']}°C")
            print(f"   Condition: {data['condition']}")
            print(f"   Note: {data['note']}")
        else:
            print(f"❌ Weather request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test cities endpoint
    print("\n7. Demo Cities")
    try:
        response = requests.get(f"{base_url}/cities")
        if response.status_code == 200:
            data = response.json()
            print("✅ Cities retrieved")
            print(f"   Total cities: {data['total']}")
            for city in data['cities'][:3]:  # Show first 3 cities
                print(f"   - {city['name']}, {city['country']} (pop: {city['population']:,})")
        else:
            print(f"❌ Cities request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test math operations
    print("\n8. Math Operations")
    math_tests = [
        ("add", "5.0", "3.0"),
        ("multiply", "7.0", "6.0"),
        ("divide", "20.0", "4.0"),
        ("power", "2.0", "8.0")
    ]
    
    for operation, a, b in math_tests:
        try:
            response = requests.get(f"{base_url}/math/{operation}/{a}/{b}")
            if response.status_code == 200:
                data = response.json()
                print(f"   {a} {operation} {b} = {data['result']}")
            else:
                print(f"   ❌ {operation} failed: {response.status_code}")
        except Exception as e:
            print(f"   ❌ {operation} error: {e}")
    
    # Test stats endpoint
    print("\n9. Statistics")
    try:
        response = requests.get(f"{base_url}/stats")
        if response.status_code == 200:
            data = response.json()
            print("✅ Statistics retrieved")
            print(f"   Total cities: {data['total_cities']}")
            print(f"   Total quotes: {data['total_quotes']}")
            print(f"   Random number: {data['random_number']}")
            print(f"   Pi: {data['pi']}")
        else:
            print(f"❌ Stats request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test error handling
    print("\n10. Error Handling")
    try:
        response = requests.get(f"{base_url}/nonexistent")
        if response.status_code == 404:
            print("✅ Error handling works correctly")
            data = response.json()
            print(f"   Error: {data['error']}")
        else:
            print(f"❌ Expected 404 but got: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n🎉 All tests completed!")


def main():
    """Main function"""
    # Get API URL from environment or use default
    api_url = os.environ.get('API_URL', 'http://localhost:8080')
    
    print(f"Testing API at: {api_url}")
    print("Note: Make sure the service is running")
    print()
    
    test_api(api_url)


if __name__ == "__main__":
    main()
