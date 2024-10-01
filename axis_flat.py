"""
Draw x, y, z axis in the Minecraft world
    x: stone
    y: grass/dirt
    z: gold
Flatten the world
    width: Size of flat world to produce.
           x, z: from -widh to width
           y: from AXIS_BOTTOM to AXIS_TOP

mc: an instance of Minecraft must be created beforehand
"""

from mcpq import Minecraft, Vec3
import param_MCJE as param

from time import sleep

mc = Minecraft()  # connect to server on localhost


def setBlocks(block_id, start, end):
    for x in range(min(start.x, end.x), max(start.x, end.x + 1)):
        for y in range(min(start.y, end.y), max(start.y, end.y + 1)):
            for z in range(min(start.z, end.z), max(start.z, end.z + 1)):
                mc.setBlock(block_id, Vec3(x, y, z))


def draw_XYZ_axis(mc, wait=0.1):
    """
    Draw xyz axis with some wait between placing each block.
    You must create mc or instance of Minecraft world beforehand.
    """
    blockTypeIdX = param.DIAMOND_BLOCK
    blockTypeIdY = param.SEA_LANTERN_BLOCK
    blockTypeIdZ = param.GOLD_BLOCK
    BLOCK_TOP_LIGHT = param.GLOWSTONE

    # x-axis
    mc.postToChat("x-axis from negative to positive region")
    x, y, z = -param.AXIS_WIDTH, param.AXIS_Y_V_ORG, 0
    while x <= param.AXIS_WIDTH:
        mc.setBlock(blockTypeIdX, Vec3(x, y, z))
        if x < 0:
            x += 2
            sleep(wait * 2)
        else:
            x += 1
            sleep(wait)
    # y-axis
    mc.postToChat("y-axis from negative to positive region")
    x, y, z = 0, param.AXIS_BOTTOM, 0
    while y <= param.AXIS_TOP - 5:
        mc.setBlock(blockTypeIdY, Vec3(x, y, z))
        if y < param.AXIS_Y_V_ORG:
            y += 2
            sleep(wait * 2)
        else:
            y += 1
            sleep(wait)
    while y <= param.AXIS_TOP:
        mc.setBlock(BLOCK_TOP_LIGHT, Vec3(x, y, z))
        y += 1
        sleep(wait)
    # z-axis
    mc.postToChat("z-axis from negative to positive region")
    x, y, z = 0, param.AXIS_Y_V_ORG, -param.AXIS_WIDTH
    while z <= param.AXIS_WIDTH:
        mc.setBlock(blockTypeIdZ, Vec3(x, y, z))
        if z < 0:
            z += 2
            sleep(wait * 2)
        else:
            z += 1
            sleep(wait)


def clear_XYZ_axis(mc, wait=0.5):
    setBlocks(param.AIR, Vec3(-param.AXIS_WIDTH, param.AXIS_Y_V_ORG, 0), Vec3(param.AXIS_WIDTH, param.AXIS_Y_V_ORG, 0))  # x
    sleep(wait)
    setBlocks(param.AIR, Vec3(0, 0, 0), Vec3(0, param.AXIS_TOP, 0))  # y
    sleep(wait)
    setBlocks(param.AIR, Vec3(0, param.AXIS_Y_V_ORG, -param.AXIS_WIDTH), Vec3(0, param.AXIS_Y_V_ORG, param.AXIS_WIDTH))  # z
    sleep(wait)


def reset_minecraft_world(mc, width=80):
    setBlocks(param.AIR, Vec3(-width, param.Y_SEA + 1, -width), Vec3(width, param.AXIS_TOP, width))
    setBlocks(param.GRASS_BLOCK, Vec3(-width, param.Y_SEA, -width), Vec3(width, param.Y_SEA,width))


if __name__ == "__main__":
    mc = Minecraft()

    mc.postToChat("axis_flat module main part")

    reset_minecraft_world(mc, width=40)
    # draw_XYZ_axis(mc, wait=0.2)
    # clear_XYZ_axis(mc, wait=0)
    draw_XYZ_axis(mc, wait=0.25)
