def main():
    userinput = float(input("Enter Temperature in Fahrenheit : "))
    
    result = (userinput - 32) * 5.0/9.0
    print(f"Temperature {userinput}°F= {result:.2f}°C")

if __name__ == "__main__":
    main()    