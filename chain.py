# consists of blocks
# blocks consist the transaction
# blocks are connected through hashing
# unique digital fingerprint - transaction + previous block's fingerprint

from blocks import Block

blockchain = []

genesis_block = Block("Chancellor on the brink...", ["i sent 2 btc, you sent 5 btc"])
second_block = Block(genesis_block.block_hash, ["i send 4 more btc"])
third_block = Block(second_block.block_hash, ["20 more btc to me"])

print(second_block.block_hash)