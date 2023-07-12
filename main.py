def main():
    with open("dataset.txt", "r") as f:
        data = f.read()
    with open("output.txt", "w") as f:
        f.write(data.upper())
    
main()