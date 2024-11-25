import bpy
import mathutils

mat = bpy.data.materials.new(name="Metal")
mat.use_nodes = True


# initialize Random x4 | Mat node group
def random_x4___mat_node_group():
    random_x4___mat = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="Random x4 | Mat"
    )

    random_x4___mat.color_tag = "NONE"
    random_x4___mat.description = ""
    random_x4___mat.default_group_node_width = 140

    # random_x4___mat interface
    # Socket 0
    _0_socket = random_x4___mat.interface.new_socket(
        name="0", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    _0_socket.default_value = 0.0
    _0_socket.min_value = 0.0
    _0_socket.max_value = 1.0
    _0_socket.subtype = "NONE"
    _0_socket.attribute_domain = "POINT"

    # Socket 1
    _1_socket = random_x4___mat.interface.new_socket(
        name="1", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    _1_socket.default_value = 0.0
    _1_socket.min_value = 0.0
    _1_socket.max_value = 1.0
    _1_socket.subtype = "NONE"
    _1_socket.attribute_domain = "POINT"

    # Socket 2
    _2_socket = random_x4___mat.interface.new_socket(
        name="2", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    _2_socket.default_value = 0.0
    _2_socket.min_value = 0.0
    _2_socket.max_value = 1.0
    _2_socket.subtype = "NONE"
    _2_socket.attribute_domain = "POINT"

    # Socket 3
    _3_socket = random_x4___mat.interface.new_socket(
        name="3", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    _3_socket.default_value = 0.0
    _3_socket.min_value = 0.0
    _3_socket.max_value = 1.0
    _3_socket.subtype = "NONE"
    _3_socket.attribute_domain = "POINT"

    # Socket 4
    _4_socket = random_x4___mat.interface.new_socket(
        name="4", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    _4_socket.default_value = 0.0
    _4_socket.min_value = -3.4028234663852886e38
    _4_socket.max_value = 3.4028234663852886e38
    _4_socket.subtype = "NONE"
    _4_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket = random_x4___mat.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    seed_socket.default_value = 0.0
    seed_socket.min_value = 0.0
    seed_socket.max_value = 1.0
    seed_socket.subtype = "NONE"
    seed_socket.attribute_domain = "POINT"

    # initialize random_x4___mat nodes
    # node Group Output
    group_output = random_x4___mat.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # node Group Input
    group_input = random_x4___mat.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # node Object Info
    object_info = random_x4___mat.nodes.new("ShaderNodeObjectInfo")
    object_info.name = "Object Info"

    # node Math
    math = random_x4___mat.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = "ADD"
    math.use_clamp = False

    # node White Noise Texture
    white_noise_texture = random_x4___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture.name = "White Noise Texture"
    white_noise_texture.noise_dimensions = "4D"

    # node Separate Color
    separate_color = random_x4___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color.name = "Separate Color"
    separate_color.mode = "RGB"

    # node Math.001
    math_001 = random_x4___mat.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = "ADD"
    math_001.use_clamp = False

    # node White Noise Texture.001
    white_noise_texture_001 = random_x4___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_001.name = "White Noise Texture.001"
    white_noise_texture_001.noise_dimensions = "4D"

    # node Separate Color.001
    separate_color_001 = random_x4___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color_001.name = "Separate Color.001"
    separate_color_001.mode = "RGB"

    # Set locations
    group_output.location = (689.6586303710938, -17.691898345947266)
    group_input.location = (-490.65618896484375, 343.00933837890625)
    object_info.location = (-490.65618896484375, 63.65891647338867)
    math.location = (-280.6562194824219, 343.00933837890625)
    white_noise_texture.location = (-70.65621948242188, 343.00933837890625)
    separate_color.location = (139.34378051757812, 343.00933837890625)
    math_001.location = (-280.6562194824219, 63.65891647338867)
    white_noise_texture_001.location = (-70.65621948242188, 63.65891647338867)
    separate_color_001.location = (139.34378051757812, 63.65891647338867)

    # Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    white_noise_texture.width, white_noise_texture.height = 140.0, 100.0
    separate_color.width, separate_color.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    white_noise_texture_001.width, white_noise_texture_001.height = 140.0, 100.0
    separate_color_001.width, separate_color_001.height = 140.0, 100.0

    # initialize random_x4___mat links
    # object_info.Random -> white_noise_texture.W
    random_x4___mat.links.new(object_info.outputs[5], white_noise_texture.inputs[1])
    # math.Value -> white_noise_texture.Vector
    random_x4___mat.links.new(math.outputs[0], white_noise_texture.inputs[0])
    # white_noise_texture.Color -> separate_color.Color
    random_x4___mat.links.new(white_noise_texture.outputs[1], separate_color.inputs[0])
    # object_info.Object Index -> math.Value
    random_x4___mat.links.new(object_info.outputs[3], math.inputs[1])
    # group_input.Seed -> math.Value
    random_x4___mat.links.new(group_input.outputs[0], math.inputs[0])
    # separate_color.Red -> group_output.0
    random_x4___mat.links.new(separate_color.outputs[0], group_output.inputs[0])
    # separate_color.Green -> group_output.1
    random_x4___mat.links.new(separate_color.outputs[1], group_output.inputs[1])
    # math_001.Value -> white_noise_texture_001.Vector
    random_x4___mat.links.new(math_001.outputs[0], white_noise_texture_001.inputs[0])
    # white_noise_texture_001.Color -> separate_color_001.Color
    random_x4___mat.links.new(
        white_noise_texture_001.outputs[1], separate_color_001.inputs[0]
    )
    # separate_color.Blue -> math_001.Value
    random_x4___mat.links.new(separate_color.outputs[2], math_001.inputs[1])
    # math.Value -> math_001.Value
    random_x4___mat.links.new(math.outputs[0], math_001.inputs[0])
    # separate_color_001.Red -> group_output.2
    random_x4___mat.links.new(separate_color_001.outputs[0], group_output.inputs[2])
    # separate_color_001.Green -> group_output.3
    random_x4___mat.links.new(separate_color_001.outputs[1], group_output.inputs[3])
    # object_info.Random -> white_noise_texture_001.W
    random_x4___mat.links.new(object_info.outputs[5], white_noise_texture_001.inputs[1])
    # separate_color_001.Blue -> group_output.4
    random_x4___mat.links.new(separate_color_001.outputs[2], group_output.inputs[4])
    return random_x4___mat


random_x4___mat = random_x4___mat_node_group()


# initialize MetalShader node group
def metalshader_node_group():
    metalshader = bpy.data.node_groups.new(type="ShaderNodeTree", name="MetalShader")

    metalshader.color_tag = "NONE"
    metalshader.description = ""
    metalshader.default_group_node_width = 140

    # metalshader interface
    # Socket BSDF
    bsdf_socket = metalshader.interface.new_socket(
        name="BSDF", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    bsdf_socket.attribute_domain = "POINT"

    # initialize metalshader nodes
    # node Group Output
    group_output_1 = metalshader.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # node Mapping.001
    mapping_001 = metalshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = "POINT"
    # Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    mapping_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Texture Coordinate.001
    texture_coordinate_001 = metalshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False
    texture_coordinate_001.outputs[0].hide = True
    texture_coordinate_001.outputs[1].hide = True
    texture_coordinate_001.outputs[2].hide = True
    texture_coordinate_001.outputs[4].hide = True
    texture_coordinate_001.outputs[5].hide = True
    texture_coordinate_001.outputs[6].hide = True

    # node Principled BSDF
    principled_bsdf = metalshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = "MULTI_GGX"
    principled_bsdf.subsurface_method = "RANDOM_WALK"
    # Metallic
    principled_bsdf.inputs[1].default_value = 0.5
    # IOR
    principled_bsdf.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    # Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf.inputs[9].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf.inputs[24].default_value = 0.0
    # Sheen Roughness
    principled_bsdf.inputs[25].default_value = 0.5
    # Sheen Tint
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf.inputs[28].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    # node Group.001
    group_001 = metalshader.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random_x4___mat
    # Socket_5
    group_001.inputs[0].default_value = 0.5999999642372131

    # node Map Range.004
    map_range_004 = metalshader.nodes.new("ShaderNodeMapRange")
    map_range_004.name = "Map Range.004"
    map_range_004.clamp = True
    map_range_004.data_type = "FLOAT"
    map_range_004.interpolation_type = "LINEAR"
    # From Min
    map_range_004.inputs[1].default_value = 0.0
    # From Max
    map_range_004.inputs[2].default_value = 1.0
    # To Min
    map_range_004.inputs[3].default_value = -1000.0
    # To Max
    map_range_004.inputs[4].default_value = 1000.0

    # node Noise Texture
    noise_texture = metalshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = "4D"
    noise_texture.noise_type = "FBM"
    noise_texture.normalize = True
    # Scale
    noise_texture.inputs[2].default_value = 2.0
    # Detail
    noise_texture.inputs[3].default_value = 15.0
    # Roughness
    noise_texture.inputs[4].default_value = 1.0
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # node Noise Texture.001
    noise_texture_001 = metalshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = "4D"
    noise_texture_001.noise_type = "FBM"
    noise_texture_001.normalize = True
    # Scale
    noise_texture_001.inputs[2].default_value = 4.0
    # Detail
    noise_texture_001.inputs[3].default_value = 10.0
    # Roughness
    noise_texture_001.inputs[4].default_value = 0.44999998807907104
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    # node Mix
    mix = metalshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = "LINEAR_LIGHT"
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = "RGBA"
    mix.factor_mode = "UNIFORM"
    # Factor_Float
    mix.inputs[0].default_value = 0.019999999552965164

    # node Voronoi Texture
    voronoi_texture = metalshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = "EUCLIDEAN"
    voronoi_texture.feature = "F1"
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = "4D"
    # Scale
    voronoi_texture.inputs[2].default_value = 10.0
    # Detail
    voronoi_texture.inputs[3].default_value = 10.0
    # Roughness
    voronoi_texture.inputs[4].default_value = 0.6000000238418579
    # Lacunarity
    voronoi_texture.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture.inputs[8].default_value = 1.0

    # node Mix.001
    mix_001 = metalshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = "LINEAR_LIGHT"
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = "RGBA"
    mix_001.factor_mode = "UNIFORM"
    # Factor_Float
    mix_001.inputs[0].default_value = 0.3333333432674408

    # node Color Ramp
    color_ramp = metalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = "RGB"
    color_ramp.color_ramp.hue_interpolation = "NEAR"
    color_ramp.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.418181836605072
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (
        0.016010019928216934,
        0.016010019928216934,
        0.016010019928216934,
        1.0,
    )

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(0.6636366844177246)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (
        0.7293347716331482,
        0.7293347716331482,
        0.7293347716331482,
        1.0,
    )

    # node Hue/Saturation/Value
    hue_saturation_value = metalshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    # Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    # node Bump
    bump = metalshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    # Strength
    bump.inputs[0].default_value = 0.05000000074505806
    # Distance
    bump.inputs[1].default_value = 1.0
    # Normal
    bump.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Math
    math_1 = metalshader.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = "MULTIPLY"
    math_1.use_clamp = False
    # Value_001
    math_1.inputs[1].default_value = 0.4000000059604645

    # node Math.001
    math_001_1 = metalshader.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = "ADD"
    math_001_1.use_clamp = False
    # Value
    math_001_1.inputs[0].default_value = 0.800000011920929

    # node Color Ramp.001
    color_ramp_001 = metalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.name = "Color Ramp.001"
    color_ramp_001.color_ramp.color_mode = "RGB"
    color_ramp_001.color_ramp.hue_interpolation = "NEAR"
    color_ramp_001.color_ramp.interpolation = "CARDINAL"

    # initialize color ramp elements
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
    color_ramp_001_cre_0.position = 0.209090918302536
    color_ramp_001_cre_0.alpha = 1.0
    color_ramp_001_cre_0.color = (
        0.5271116495132446,
        0.5271156430244446,
        0.5271153450012207,
        1.0,
    )

    color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.25909096002578735)
    color_ramp_001_cre_1.alpha = 1.0
    color_ramp_001_cre_1.color = (
        0.6307530999183655,
        0.6307578682899475,
        0.6307575702667236,
        1.0,
    )

    # Set locations
    group_output_1.location = (2044.083740234375, -366.00262451171875)
    mapping_001.location = (-1194.0040283203125, -136.5179443359375)
    texture_coordinate_001.location = (-1403.3446044921875, -27.531539916992188)
    principled_bsdf.location = (1600.194091796875, -191.6177520751953)
    group_001.location = (-1918.9130859375, -195.75552368164062)
    map_range_004.location = (-1622.7310791015625, -136.37307739257812)
    noise_texture.location = (63.203857421875, -115.5820083618164)
    noise_texture_001.location = (-408.960693359375, -66.52783966064453)
    mix.location = (-156.0946044921875, -106.74933624267578)
    voronoi_texture.location = (-887.256591796875, 158.18812561035156)
    mix_001.location = (-661.845703125, 37.20197296142578)
    color_ramp.location = (672.6860961914062, -25.041709899902344)
    hue_saturation_value.location = (1040.343994140625, -15.05459213256836)
    bump.location = (924.097900390625, -349.8353271484375)
    math_1.location = (318.8853759765625, 59.16470718383789)
    math_001_1.location = (493.6171875, 119.59449005126953)
    color_ramp_001.location = (1326.2567138671875, 107.00934600830078)

    # Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    mapping_001.width, mapping_001.height = 140.0, 100.0
    texture_coordinate_001.width, texture_coordinate_001.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    map_range_004.width, map_range_004.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    noise_texture_001.width, noise_texture_001.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    voronoi_texture.width, voronoi_texture.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0
    color_ramp.width, color_ramp.height = 240.0, 100.0
    hue_saturation_value.width, hue_saturation_value.height = 150.0, 100.0
    bump.width, bump.height = 140.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    color_ramp_001.width, color_ramp_001.height = 240.0, 100.0

    # initialize metalshader links
    # texture_coordinate_001.Object -> mapping_001.Vector
    metalshader.links.new(texture_coordinate_001.outputs[3], mapping_001.inputs[0])
    # map_range_004.Result -> mapping_001.Location
    metalshader.links.new(map_range_004.outputs[0], mapping_001.inputs[1])
    # group_001.0 -> map_range_004.Value
    metalshader.links.new(group_001.outputs[0], map_range_004.inputs[0])
    # mix.Result -> noise_texture.Vector
    metalshader.links.new(mix.outputs[2], noise_texture.inputs[0])
    # noise_texture_001.Color -> mix.B
    metalshader.links.new(noise_texture_001.outputs[1], mix.inputs[7])
    # mapping_001.Vector -> mix.A
    metalshader.links.new(mapping_001.outputs[0], mix.inputs[6])
    # mapping_001.Vector -> voronoi_texture.Vector
    metalshader.links.new(mapping_001.outputs[0], voronoi_texture.inputs[0])
    # mapping_001.Vector -> mix_001.A
    metalshader.links.new(mapping_001.outputs[0], mix_001.inputs[6])
    # voronoi_texture.Distance -> mix_001.B
    metalshader.links.new(voronoi_texture.outputs[0], mix_001.inputs[7])
    # mix_001.Result -> noise_texture_001.Vector
    metalshader.links.new(mix_001.outputs[2], noise_texture_001.inputs[0])
    # color_ramp.Color -> hue_saturation_value.Color
    metalshader.links.new(color_ramp.outputs[0], hue_saturation_value.inputs[4])
    # hue_saturation_value.Color -> principled_bsdf.Roughness
    metalshader.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    # principled_bsdf.BSDF -> group_output_1.BSDF
    metalshader.links.new(principled_bsdf.outputs[0], group_output_1.inputs[0])
    # bump.Normal -> principled_bsdf.Normal
    metalshader.links.new(bump.outputs[0], principled_bsdf.inputs[5])
    # noise_texture.Color -> color_ramp.Fac
    metalshader.links.new(noise_texture.outputs[1], color_ramp.inputs[0])
    # noise_texture.Color -> bump.Height
    metalshader.links.new(noise_texture.outputs[1], bump.inputs[2])
    # group_001.1 -> noise_texture_001.W
    metalshader.links.new(group_001.outputs[1], noise_texture_001.inputs[1])
    # group_001.2 -> noise_texture.W
    metalshader.links.new(group_001.outputs[2], noise_texture.inputs[1])
    # group_001.3 -> voronoi_texture.W
    metalshader.links.new(group_001.outputs[3], voronoi_texture.inputs[1])
    # group_001.4 -> math_1.Value
    metalshader.links.new(group_001.outputs[4], math_1.inputs[0])
    # math_1.Value -> math_001_1.Value
    metalshader.links.new(math_1.outputs[0], math_001_1.inputs[1])
    # math_001_1.Value -> hue_saturation_value.Value
    metalshader.links.new(math_001_1.outputs[0], hue_saturation_value.inputs[2])
    # color_ramp_001.Color -> principled_bsdf.Base Color
    metalshader.links.new(color_ramp_001.outputs[0], principled_bsdf.inputs[0])
    # hue_saturation_value.Color -> color_ramp_001.Fac
    metalshader.links.new(hue_saturation_value.outputs[0], color_ramp_001.inputs[0])
    return metalshader


metalshader = metalshader_node_group()


# initialize Metal node group
def metal_node_group():
    metal = mat.node_tree
    # start with a clean node tree
    for node in metal.nodes:
        metal.nodes.remove(node)
    metal.color_tag = "NONE"
    metal.description = ""
    metal.default_group_node_width = 140

    # metal interface

    # initialize metal nodes
    # node Material Output
    material_output = metal.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = "ALL"
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0

    # node Group.006
    group_006 = metal.nodes.new("ShaderNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = metalshader

    # Set locations
    material_output.location = (-63.728790283203125, -75.2525634765625)
    group_006.location = (-481.5697021484375, -96.51497650146484)

    # Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    group_006.width, group_006.height = 269.610107421875, 100.0

    # initialize metal links
    # group_006.BSDF -> material_output.Surface
    metal.links.new(group_006.outputs[0], material_output.inputs[0])
    return metal


metal = metal_node_group()
