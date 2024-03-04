import java.io.*;

class crc_gen {
    static int[] divide(int div[], int divisor[], int rem[]) {
        int cur = 0;
        while (true) {
            for (int i = 0; i < divisor.length; i++)
                rem[cur + i] = (rem[cur + i] ^ divisor[i]);

            while (rem[cur] == 0 && cur != rem.length - 1)
                cur++;

            if ((rem.length - cur) < divisor.length)
                break;
        }
        return rem;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] data;
        int[] div;
        int[] divisor;
        int[] rem;
        int[] crc;
        int data_bits, divisor_bits, tot_length;

        System.out.println("Enter number of data bits : ");
        data_bits = Integer.parseInt(br.readLine());
        data = new int[data_bits];

        System.out.println("Enter data bits : ");
        for (int i = 0; i < data_bits; i++)
            data[i] = Integer.parseInt(br.readLine());

        System.out.println("Enter number of bits in divisor : ");
        divisor_bits = Integer.parseInt(br.readLine());
        divisor = new int[divisor_bits];

        System.out.println("Enter Divisor bits : ");
        for (int i = 0; i < divisor_bits; i++)
            divisor[i] = Integer.parseInt(br.readLine());

        tot_length = data_bits + divisor_bits - 1;

        div = new int[tot_length];
        rem = new int[tot_length];
        crc = new int[tot_length];
        for (int i = 0; i < data.length; i++)
            div[i] = data[i];

        System.out.print("Dividend (after appending 0's) are : ");
        for (int i = 0; i < div.length; i++)
            System.out.print(div[i]);
        System.out.println();

        for (int j = 0; j < div.length; j++) {
            rem[j] = div[j];
        }

        rem = divide(div, divisor, rem);

        for (int i = 0; i < div.length; i++) {
            crc[i] = (div[i] ^ rem[i]);
        }

        System.out.println();
        System.out.println("CRC code : ");
        for (int i = 0; i < crc.length; i++)
            System.out.print(crc[i]);

        System.out.println();
        System.out.println("Enter CRC code of " + tot_length + " bits : ");
        for (int i = 0; i < crc.length; i++)
            crc[i] = Integer.parseInt(br.readLine());
        for (int j = 0; j < crc.length; j++) {
            rem[j] = crc[j];
        }

        rem = divide(crc, divisor, rem);

        for (int i = 0; i < rem.length; i++) {
            if (rem[i] != 0) {
                System.out.println("Error");
                break;
            }
            if (i == rem.length - 1)
                System.out.println("No Error");
        }

        System.out.println("THANK YOU.... :)");
    }

}



This Java program implements the CRC (Cyclic Redundancy Check) generation and verification algorithm. Here's a breakdown of how it works:

1. It defines a class `crc_gen` with a main method.
2. The main method takes input from the user for the number of data bits and the data bits themselves.
3. It also takes input for the number of bits in the divisor and the divisor bits.
4. It appends 0's to the data to match the length of the divisor.
5. It performs the division operation to generate the CRC code.
6. It prints the generated CRC code.
7. It takes input from the user for the received CRC code.
8. It performs the division operation on the received CRC code.
9. It checks if the remainder obtained after division is all zeros, indicating no error, or if there's a non-zero remainder, indicating an error.
10. It prints the result - whether there's an error or not.

This program demonstrates how CRC codes can be generated and verified to detect errors in data transmission. If you have any questions or need further clarification, feel free to ask!


The `divide` function in the CRC generation Java program is responsible for performing the polynomial division operation required to generate the CRC code. Let's break down the function in detail:

```java
static int[] divide(int div[], int divisor[], int rem[]) {
    int cur = 0;
    while (true) {
        for (int i = 0; i < divisor.length; i++)
            rem[cur + i] = (rem[cur + i] ^ divisor[i]);

        while (rem[cur] == 0 && cur != rem.length - 1)
            cur++;

        if ((rem.length - cur) < divisor.length)
            break;
    }
    return rem;
}
```

- **Parameters**:
  - `div[]`: The dividend, which is the data bits appended with zeros to match the length of the divisor.
  - `divisor[]`: The divisor, which is the polynomial representing the CRC generator.
  - `rem[]`: The remainder, initially set to the dividend.

- **Return Type**: The function returns an array representing the remainder after polynomial division.

- **Functionality**:
  1. **Initialization**: The function starts by initializing a variable `cur` to 0, which represents the current position in the dividend.
  2. **Division Loop**: The function enters a `while` loop that continues indefinitely (`true`) until it's explicitly terminated by a `break` statement.
     - Inside the loop, it iterates over each coefficient of the divisor polynomial.
       - For each coefficient, it performs the XOR operation between the corresponding coefficients of the remainder (`rem`) and the divisor polynomial.
       - This simulates the polynomial division operation, where the remainder is updated by subtracting the divisor polynomial from it.
     - After updating the remainder, it checks for leading zeros in the remainder.
       - If there are leading zeros, it increments the `cur` variable until it reaches the first non-zero coefficient or the end of the remainder.
       - This step ensures that the remainder is shifted to the left to remove any leading zeros.
     - It checks if the remaining length of the remainder (from the current position `cur` to the end) is less than the length of the divisor polynomial.
       - If the remaining length is less than the length of the divisor, it breaks out of the loop since further division is not possible.
  3. **Return**: Finally, the function returns the updated remainder array after completing the division operation.

- **Usage**:
  - The `divide` function is called within the main program to perform polynomial division during both CRC generation and CRC verification phases.

Overall, the `divide` function implements the core logic of polynomial division required for CRC generation and verification, efficiently updating the remainder and handling leading zeros to ensure accurate division results.