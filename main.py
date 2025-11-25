from detector import JaundiceDetector

if __name__ == "__main__":
    try:
        app = JaundiceDetector()
        app.run()
    except Exception as e:
        print("An error occurred:", str(e))
