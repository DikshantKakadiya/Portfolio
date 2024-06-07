from Crypto.Cipher import AES
import base64

# Define the encrypted message and the key
encrypted_message = "9gTG99KTHBwoGQIsYPUuV2KqOMP1pO/zmnFR5QyrhXbgOfaxxibQSLVf8fxoRbuXuIro9iKXgtPahWevU/HONtdJ74RuNmu6UNFjHNydIrq8BjO6aMogsTEZWYST0AtiHIkIl4lykZT8xwb28ol3vhtuDHLnt5rtUiCcUmUHaqf5U/4Ud+oxvVOgTWxy9IoIaxL9K6vwK2/DKHbz+d4QGlA+DqXbHDrZxyvtteOPfsHrPSPBlDkVposFigJwflVF2YduDLF/5iSNTfoNudr7suZLvM+lLPjrCcFxJZETYTFf/VHuXj8khBTxXArXSi9MIDE4GELm7UOnE9JOf++FPW400kiYBSX28ELi4OJhsuIxtKUKkwkDXqg4Zjd4n7pBR43GFtskS9csaMRD3LByy7Yf/gL+RxwWinkiLtb33wVk4qRpp7eilY/jSiv84KARmOF4EKUC5Pqy9PrJIv1OrfjuBMK++oThjRkM6BAbSJy8+tcyxUjiKgcygKNh/5poEK3/13lnhL2DTrRUPeGS5q8D6hYFZwBSWhfOmhuBEL7Aih/mPcD1AVjyec+k6/5PxZT3Qckf+biEL7/PG5LBPWrn3mtL6x8S2RH9/J/Z3kawOmAPW33ZRWhy5EhcaL5g0TlubmoKxKiLSqhoDqcVd+3vOI1er3tpR0uWVuMEoPSw7S83n+9K6/cVXurZ0QGC88OtT3iwWaILAzT1bR1YD0bd0ePUfZHdxws0HPPfjZnP+aCkjy3A2TugjZa3yPNuUoGHEzR0fkgTpZX9/gCghQVGREpwO3Iv22bUsKd0a67cpbIF26BA2QYsYMZedIMFawH0f5teV9DzAH0ARHz34OBLi1flNUrnLAoZy0kdPtt8wKC8CvFwZjIbr9p0bTe6fIxvQyZO57aAJcrzhzKUVrpS+ysLO8iCkZB6sC4hpZc0daZnXdECoiYcGebT5m19jTqAt9ZVmNnXN4dyI6K/0xwAhbYygSz3sUwuftnjeRFlzYCFdAut9n7T3otZoi7kmbzLiCpsrXWl5txVDppjZ9HsrGDDIn4Ox1kCZws1sxNsOf9qyx4F7vVhmaZOeatSvvkLIcxN9Nkonwc+E/is70ciuha4s6hH+u7ZpF9etldh5H2wM8fDQ+tsGRDntlat2vECbe12udzIlDg8bNNyepr0hxz6KkV7XFtwG7243HGSWwOTal4zaS831bGbcL5Z21RX4hl/BEYIuhD/q4fFUkxHQgUU01dsEQlY4D6QE9UzTe5BLvJ4u3tLIRDRll5kBuM9OgmwgleuaG38yB2NS13Uv1llXx8GP//khRDhXsc4KQ7hklsmQJA88tf/APETkpb1X6E8LvkY/o+lc4xkTItY3JbBwCOrRdIHNqdzyxBXw/i0ffyx6ic8POrZFuB/NMs6nRsRS8ThQuYJSvpxDpkoaEX/C2BCBlatsjH44ZbprKJ8UCdYudfFiKSusGdNMd0YSSIXPesr2e8CbDMGeFbiaK4mSLaWl139nvmiUg2RvINewzjRWk7/TmyoVGC1gmHFzxcmgpo3NRUGXYsxF3QNQbcZyKnTWw3yO7Cbx+TX0vx+H36E3OYwhajK9BTS"
key = "E1691A9ADE186DF855561A6264A84685"

# Decode the encrypted message from base64
decoded_message = base64.b64decode(encrypted_message)

# Create an AES cipher object with CBC mode
cipher = AES.new(key.encode(), AES.MODE_CBC, iv=decoded_message[:16])

# Decrypt the message
decrypted_message = cipher.decrypt(decoded_message[16:])

# Remove padding
decrypted_message = decrypted_message[:-decrypted_message[-1]]

# Print the decrypted message
print(decrypted_message.decode())