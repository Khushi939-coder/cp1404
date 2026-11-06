from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    my_guitars = read_file(FILENAME)
    my_guitars.sort()
    print("The Guitar Collection (Oldest to Newest):")
    for guitar in my_guitars:
        print(guitar)

    add_guitars(FILENAME, my_guitars)


def read_file(FILENAME):
    with open(FILENAME) as r:
        guitars = []
        for line in r:
            parts = line.split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
        return guitars

def add_guitars(FILENAME, guitars):
    new_guitars = []
    while True:
        name = input("Enter guitar name (or type 'done' to exit): ")
        if name.lower() == "done":
            break

        try:
           year = int(input("Enter guitar year: "))
           cost = float(input("Enter guitar cost: "))
           new_guitar = Guitar(name, year, cost)
           guitars.append(new_guitar)
        except ValueError:
           print("Invalid input")

    with open(FILENAME, 'a') as f:
        for guitar in guitars:
            f.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

    print("Guitars added successfully")


if __name__ == "__main__":
    main()


