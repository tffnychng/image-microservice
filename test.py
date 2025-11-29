import requests
from PIL import Image
import io
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import json

def main():
    print("Testing microservice with sample cover (Eusexua by FKA Twigs)")
    
    test_url = "https://i.scdn.co/image/ab67616d0000b273755b26e3af91368d71a150ab"  
    
    try:
        print(f"Testing with URL: {test_url}")
        
        response = requests.post(
            "http://localhost:5001/api/cover/process",
            json={"image_url": test_url, "size": 200}
        )
        result = response.json()
        
        if result["status"] == "success":
            print("Processing successful")
            print(f"Dimensions: {result['dimensions']}")
            print(f"Format: {result['format']}")
            image_data = bytes.fromhex(result["image_data"])
            with open("test_output.jpeg", "wb") as f:
                f.write(image_data)
            print("Saved as: test_output.jpeg")
        else:
            print("Processing failed")
            print(f"Error: {result.get('message')}")
        
            
    except requests.exceptions.ConnectionError:
        print("Can't connect to microservice")
    except Exception as e:
        print(f"Test failed with error: {e}")

if __name__ == "__main__":
        main()
              