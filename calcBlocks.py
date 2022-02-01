#If a filesystem has a block size of 4096 bytes, this means that a file comprised 
#of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes 
#will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the 
#blocks function below, which calculates the storage size needed for a given filesize?

def blocks(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    print "full_blocks: ",full_blocks
    # Use the modulo operator to check whether there's any remainder
    partial_block = filesize % block_size
    print "partial_block: ",partial_block

    # Depending on whether there's a remainder or not, return the right number.
    if partial_block > 0:
    	if full_blocks > 0:
        	return (full_blocks * block_size) + (partial_block * block_size)
        else:
        	return (partial_block * block_size)
    elif (full_blocks > 0):
    	return full_blocks * block_size

print(blocks(1))    # Should be 4096
print(blocks(4096)) # Should be 4096
print(blocks(4097)) # Should be 8192
print(blocks(190))