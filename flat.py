from mcpq import Minecraft, Vec3

mc = Minecraft()  # connect to server on localhost

mc.postToChat("Hello Minecraft!")

def setBlocks(block_id, start, end):
    positions = []
    for x in range(min(start.x, end.x), max(start.x, end.x + 1)):
        for y in range(min(start.y, end.y), max(start.y, end.y + 1)):
            for z in range(min(start.z, end.z), max(start.z, end.z + 1)):
                positions.append(Vec3(x, y, z))
    mc.setBlockList(block_id, positions)

# setBlocks("air", Vec3(-40, 63, -40), Vec3(40, 120, 40))
# setBlocks("gold_block", Vec3(-40, 62, -40), Vec3(40, 62, 40))
# setBlocks("grass_block", Vec3(-40, 62, -40), Vec3(40, 62, 40))

# mc.setBlockCube("air", Vec3(-40, 63, -40), Vec3(40, 120, 40))
# mc.setBlockCube("air", Vec3(-40, 75, -40), Vec3(40, 70, 40))
mc.setBlockCube("grass_block", Vec3(-40, 62, -40), Vec3(40, 62, 40))

