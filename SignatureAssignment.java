import java.io.*;
import java.security.*;
import java.security.interfaces.*;
import java.security.spec.*;


public class SignatureAssignment {
	// public static byte[] loadFile(String filename) {
	// 	File file = new File(filename);
	// 	byte[] data = new byte[(int) file.length()];
	// 	try (FileInputStream fis = new FileInputStream(file)) {
	// 		fis.read(data);
	// 	} catch (IOException e) {
	// 		e.printStackTrace();
	// 		return null;
	// 	}

	// 	return data;
	// }
	public byte[] loadFile(String filename) {
		byte[] data = null;
		FileInputStream fis = null;
		try {
			File f = new File(filename);
			fis = new FileInputStream(f);
			data = new byte[(int) f.length()];
			fis.read(data);
			fis.close();
		} catch (FileNotFoundException ex) {
			System.err.println("Unable to open "+filename);
			return null;
		} catch (IOException ex) {
			System.err.println("Unable to open "+filename);
			return null;
		} finally {
			if (fis != null) {
				try {
					fis.close();
				} catch (Exception e) {
					// ignore
				}
			}
		}
		return data;
	}
	
	// public static PublicKey loadPublicKey(String filename) {
	// 	try {
	// 		// Read public key bytes from file
	// 		InputStream in = new FileInputStream(filename);
	// 		byte[] publicKeyBytes = new byte[in.available()];
	// 		in.read(publicKeyBytes);
	// 		in.close();
			
	// 		// Convert public key bytes into a PublicKey object
	// 		X509EncodedKeySpec keySpec = new X509EncodedKeySpec(publicKeyBytes);
	// 		KeyFactory keyFactory = KeyFactory.getInstance("RSA");
	// 		PublicKey publicKey = keyFactory.generatePublic(keySpec);
			
	// 		return publicKey;
	// 	} catch (Exception e) {
	// 		e.printStackTrace();
	// 		return null;
	// 	}
	// }
	
	public PublicKey loadKey(String filename) {	
		byte[] data = loadFile(filename);
		if (data == null) {
			System.err.println("Unable to load key file.");
			return null;
		}
		X509EncodedKeySpec x509 = new X509EncodedKeySpec(data);
		PublicKey pub = null;
		try {
			KeyFactory kf = KeyFactory.getInstance("RSA");
			pub = kf.generatePublic(x509);
		} catch (NoSuchAlgorithmException e) {
			System.err.println(e);
			return null;
		} catch (InvalidKeySpecException e) {
			System.err.println(e);
			return null;
		}
		return pub;
	}
	
	/**
	* Check if pdfFile was signed by keyFile, resulting in sigFile
	* @param keyFile File containing the DER-encoded key
	* @param sigFile File containing the signature
	* @param pdfFile File containing pdf
	* @return true of everything matches, false otherwise.
	*/
	public boolean check(String keyFile, String sigFile, String pdfFile) {
		PublicKey pub = loadKey(keyFile);
		if (pub == null) {
			return false;
		}
		byte[] sigData = loadFile(sigFile);
		if (sigData == null) {
			return false;
		}
		byte[] pdfData = loadFile(pdfFile);
		if (pdfData == null) {
			return false;
		}
		try {
			Signature sig = Signature.getInstance("SHA1withRSA");
			sig.initVerify(pub);
			sig.update(pdfData);
			return sig.verify(sigData);
		} catch (NoSuchAlgorithmException e) {
			System.err.println(e);
			return false;
		} catch (InvalidKeyException e) {
			System.err.println(e);
			return false;
		} catch (SignatureException e) {
			System.err.println(e);
			return false;
		}
	}
	
	public static void main(String args[]) {
		SignatureAssignment sigTester = new SignatureAssignment();
		String[] pdfs = {"wizardofoz.pdf", "dracula.pdf"};
		String[] keys = {"key1.pub.der", "key2.pub", "key3.pub", "key4.pub", "key5.pub"};
		String sigFile = "signature.sig";
		for (String pdf : pdfs) {
			for (String key : keys) {
				if (sigTester.check(key, sigFile, pdf)) {
					System.out.println(pdf + " was signed by " + key);
					return;
				}
			}
			System.out.println("No valid signature found.");
		}
	}
}

