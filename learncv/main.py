# print("reaching here")
import arithmetic
import playwithpixels
import readimage
# print("reaching here")


def main():
    print("Raeching here")
    functions = dict()
    functions[1] = readimage.main
    functions[2] = playwithpixels.main
    functions[3] = arithmetic.main
    print("Reachign here")

    continueFlag = True
    while continueFlag:
        print("Please input file number: ")
        print("1. Read and write images")
        print("2. Manipulate pixels")
        print("3. Perform arithmetic operations")
        response = input("Number: ")
        if response == 1:
            functions[1]()
        elif response == 2:
            functions[2]()
        elif respones == 3:
            functions[3]()

        keepGoing = input("Continue? [Y/n]")
        if keepGoing == "y" or keepGoing == "Y":
            continue
        else:
            break
        



if __name__ == "__main__":
    main()