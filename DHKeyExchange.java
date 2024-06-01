import java.math.BigInteger;

public class DHKeyExchange {
    public static void main(String[] args) {
        // Diffie-Hellman parameters
        BigInteger p = new BigInteger("00fb2e8473c499d184d806e6b5df7f621b", 16);
        BigInteger alpha = BigInteger.valueOf(2);
        BigInteger keyA = new BigInteger("2ca50afea541f0d90f68e0efc85c2686", 16);
        BigInteger keyB = new BigInteger("6e146d3b2149f41450713e5c83d21e70", 16);

        // Determine the number of bits in p
        int bitCount = p.bitLength();
        System.out.println("Bit count of p: " + bitCount);

        // Alice and Bob establish their shared key
        BigInteger sharedKeyA = keyB.modPow(keyA, p);
        BigInteger sharedKeyB = keyA.modPow(keyB, p);

        // Convert shared keys to hexadecimal strings
        String sharedKeyAHex = sharedKeyA.toString(16);
        String sharedKeyBHex = sharedKeyB.toString(16);

        // Add leading zeros if necessary
        sharedKeyAHex = String.format("%32s", sharedKeyAHex).replace(' ', '0');
        sharedKeyBHex = String.format("%32s", sharedKeyBHex).replace(' ', '0');

        System.out.println("Shared key A  : " + sharedKeyAHex);
        System.out.println("Shared key B  : " + sharedKeyBHex);
    }
}
