def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

def main() -> int:
    ## input
    with open("test0.txt", "r") as f:
        textIn = f.readlines()

    prettyPrint(textIn)
    
    return 

if __name__ == '__main__':
    print(f'The answer is: {main()}')