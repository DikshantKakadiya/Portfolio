import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
//import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class AES {
    
    private static final String CIPHER_ALGORITHM = "AES/CBC/PKCS5Padding";
    private static final byte[] KEY_BYTES = {4, 2, 1};
    private static final byte[] IV_BYTES = {1, 2, 4};

    public static void main(String[] args) throws Exception {
         // Input plaintext string
        String plaintext = "World!";

        // Encrypt plaintext using CBC cipher
        byte[] cbcCiphertextBytes = encryptCBC(plaintext);

        // Encrypt plaintext using ECB cipher
        byte[] ecbCiphertextBytes = encryptECB(plaintext);

        // Convert ciphertext to hexadecimal string
        String ecbCiphertextHex = bytesToHex(ecbCiphertextBytes);
        String cbcCiphertextHex = bytesToHex(cbcCiphertextBytes);

        // Print output
        System.out.println("ECB: " + ecbCiphertextHex);
        System.out.println("CBC: " + cbcCiphertextHex);

        // Verify that the plaintext can be decrypted correctly
        String cbcPlaintext = decryptCBC(cbcCiphertextBytes);
        String ecbPlaintext = decryptECB(ecbCiphertextBytes);

        assert plaintext.equals(cbcPlaintext);
        assert plaintext.equals(ecbPlaintext);
     }
    
     private static String bytesToHex(byte[] cbcCiphertextBytes) {
        return null;
    }

    public static byte[] encryptCBC(String plaintext) throws Exception {
        // Convert plaintext to byte array
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);

        // Create key and IV
        SecretKeySpec keySpec = new SecretKeySpec(KEY_BYTES, "AES");
        IvParameterSpec ivSpec = new IvParameterSpec(IV_BYTES);

        // Create CBC cipher
        Cipher cipher = Cipher.getInstance(CIPHER_ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, keySpec, ivSpec);

        // Encrypt plaintext using CBC cipher
        return cipher.doFinal(plaintextBytes);
     }

     public static byte[] encryptECB(String plaintext) throws Exception {
        // Convert plaintext to byte array
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);

        // Create key
        SecretKeySpec keySpec = new SecretKeySpec(KEY_BYTES, "AES");

        // Create ECB cipher
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, keySpec);

        // Encrypt plaintext using ECB cipher
        return cipher.doFinal(plaintextBytes);
     }

     public static String decryptCBC(byte[] ciphertextBytes) throws Exception {
        // Create key and IV
        SecretKeySpec keySpec = new SecretKeySpec(KEY_BYTES, "AES");
        IvParameterSpec ivSpec = new IvParameterSpec(IV_BYTES);

        // Create CBC cipher
        Cipher cipher = Cipher.getInstance(CIPHER_ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, keySpec, ivSpec);

        // Decrypt ciphertext using CBC cipher
        byte[] decryptedBytes = cipher.doFinal(ciphertextBytes);
        return new String(decryptedBytes, StandardCharsets.UTF_8);
     }

     public static String decryptECB(byte[] ciphertextBytes) throws Exception {
        // Create key
        SecretKeySpec keySpec = new SecretKeySpec(KEY_BYTES, "AES");
     }
}
    
