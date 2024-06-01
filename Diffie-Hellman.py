import hashlib

p = 0x00fb2e8473c499d184d806e6b5df7f621b
alpha = 2
k_priv_Alice = 0x2ca50afea541f0d90f68e0efc85c2686
k_priv_Bob = 0x6e146d3b2149f41450713e5c83d21e70

# Determine the number of bits in p
bit_count = p.bit_length()
print("Bit count of p:", bit_count)

# Alice computes her public key
k_pub_Alice = pow(alpha, k_priv_Alice, p)

# Bob computes his public key
k_pub_Bob = pow(alpha, k_priv_Bob, p)

# Alice and Bob exchange public keys and compute the shared key
shared_key_Alice = pow(k_pub_Bob, k_priv_Alice, p)
shared_key_Bob = pow(k_pub_Alice, k_priv_Bob, p)

# Convert the shared key to a string
shared_key_str = hex(shared_key_Alice)[2:].rstrip("L").zfill(32)

# Print the shared keys
print("Shared key A  :", shared_key_str)
print("Shared key B  :", shared_key_str)
