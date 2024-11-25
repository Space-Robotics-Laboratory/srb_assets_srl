import bpy
import mathutils

mat = bpy.data.materials.new(name="SolarPanel")
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


# initialize SolarPanelShader node group
def solarpanelshader_node_group():
    solarpanelshader = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="SolarPanelShader"
    )

    solarpanelshader.color_tag = "NONE"
    solarpanelshader.description = ""
    solarpanelshader.default_group_node_width = 140

    # solarpanelshader interface
    # Socket BSDF
    bsdf_socket = solarpanelshader.interface.new_socket(
        name="BSDF", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    bsdf_socket.attribute_domain = "POINT"

    # initialize solarpanelshader nodes
    # node Group Output
    group_output_1 = solarpanelshader.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # node Frame.002
    frame_002 = solarpanelshader.nodes.new("NodeFrame")
    frame_002.label = "Roughness"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # node Frame.003
    frame_003 = solarpanelshader.nodes.new("NodeFrame")
    frame_003.label = "Bump"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # node Frame.001
    frame_001 = solarpanelshader.nodes.new("NodeFrame")
    frame_001.label = "Blue Texture"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # node Frame
    frame = solarpanelshader.nodes.new("NodeFrame")
    frame.label = "Grid Texture"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # node Noise Texture
    noise_texture = solarpanelshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = "4D"
    noise_texture.noise_type = "FBM"
    noise_texture.normalize = True
    # Scale
    noise_texture.inputs[2].default_value = 6.0
    # Detail
    noise_texture.inputs[3].default_value = 14.999999046325684
    # Roughness
    noise_texture.inputs[4].default_value = 0.550000011920929
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # node Mix.001
    mix_001 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = "DARKEN"
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = "RGBA"
    mix_001.factor_mode = "UNIFORM"
    # B_Color
    mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)

    # node Bump.001
    bump_001 = solarpanelshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = True
    # Distance
    bump_001.inputs[1].default_value = 1.0
    # Normal
    bump_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node ColorRamp.004
    colorramp_004 = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp_004.name = "ColorRamp.004"
    colorramp_004.color_ramp.color_mode = "RGB"
    colorramp_004.color_ramp.hue_interpolation = "NEAR"
    colorramp_004.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_004.color_ramp.elements.remove(colorramp_004.color_ramp.elements[0])
    colorramp_004_cre_0 = colorramp_004.color_ramp.elements[0]
    colorramp_004_cre_0.position = 0.24025972187519073
    colorramp_004_cre_0.alpha = 1.0
    colorramp_004_cre_0.color = (
        0.20731863379478455,
        0.20731863379478455,
        0.20731863379478455,
        1.0,
    )

    colorramp_004_cre_1 = colorramp_004.color_ramp.elements.new(0.8545454740524292)
    colorramp_004_cre_1.alpha = 1.0
    colorramp_004_cre_1.color = (
        0.9054436087608337,
        0.9054436087608337,
        0.9054436087608337,
        1.0,
    )

    # node Reroute.001
    reroute_001 = solarpanelshader.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketVector"
    # node Reroute
    reroute = solarpanelshader.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVector"
    # node ColorRamp.001
    colorramp_001 = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp_001.name = "ColorRamp.001"
    colorramp_001.color_ramp.color_mode = "RGB"
    colorramp_001.color_ramp.hue_interpolation = "NEAR"
    colorramp_001.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_001.color_ramp.elements.remove(colorramp_001.color_ramp.elements[0])
    colorramp_001_cre_0 = colorramp_001.color_ramp.elements[0]
    colorramp_001_cre_0.position = 0.4724999964237213
    colorramp_001_cre_0.alpha = 1.0
    colorramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_001_cre_1 = colorramp_001.color_ramp.elements.new(0.48500001430511475)
    colorramp_001_cre_1.alpha = 1.0
    colorramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Voronoi Texture
    voronoi_texture = solarpanelshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = "CHEBYCHEV"
    voronoi_texture.feature = "F1"
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = "3D"
    # Scale
    voronoi_texture.inputs[2].default_value = 2.0
    # Detail
    voronoi_texture.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture.inputs[8].default_value = 0.0

    # node Voronoi Texture.001
    voronoi_texture_001 = solarpanelshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = "MANHATTAN"
    voronoi_texture_001.feature = "F1"
    voronoi_texture_001.normalize = False
    voronoi_texture_001.voronoi_dimensions = "3D"
    # Scale
    voronoi_texture_001.inputs[2].default_value = 2.0
    # Detail
    voronoi_texture_001.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_001.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture_001.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture_001.inputs[8].default_value = 0.0

    # node ColorRamp
    colorramp = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = "RGB"
    colorramp.color_ramp.hue_interpolation = "NEAR"
    colorramp.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.4749999940395355
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (1.0, 1.0, 1.0, 1.0)

    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.48500001430511475)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.0, 0.0, 0.0, 1.0)

    # node Vector Math
    vector_math = solarpanelshader.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = "ADD"
    # Vector_001
    vector_math.inputs[1].default_value = (0.75, 0.75, 0.0)

    # node Mix
    mix = solarpanelshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = "DARKEN"
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = "RGBA"
    mix.factor_mode = "UNIFORM"
    # Factor_Float
    mix.inputs[0].default_value = 1.0

    # node Voronoi Texture.002
    voronoi_texture_002 = solarpanelshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_002.name = "Voronoi Texture.002"
    voronoi_texture_002.distance = "EUCLIDEAN"
    voronoi_texture_002.feature = "F1"
    voronoi_texture_002.normalize = False
    voronoi_texture_002.voronoi_dimensions = "4D"
    # Scale
    voronoi_texture_002.inputs[2].default_value = 130.0
    # Detail
    voronoi_texture_002.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_002.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture_002.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture_002.inputs[8].default_value = 1.0

    # node Noise Texture.001
    noise_texture_001 = solarpanelshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = "4D"
    noise_texture_001.noise_type = "FBM"
    noise_texture_001.normalize = True
    # Scale
    noise_texture_001.inputs[2].default_value = 2.0
    # Detail
    noise_texture_001.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_001.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    # node ColorRamp.006
    colorramp_006 = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp_006.name = "ColorRamp.006"
    colorramp_006.color_ramp.color_mode = "RGB"
    colorramp_006.color_ramp.hue_interpolation = "NEAR"
    colorramp_006.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_006.color_ramp.elements.remove(colorramp_006.color_ramp.elements[0])
    colorramp_006_cre_0 = colorramp_006.color_ramp.elements[0]
    colorramp_006_cre_0.position = 0.002597402548417449
    colorramp_006_cre_0.alpha = 1.0
    colorramp_006_cre_0.color = (0.0, 0.027247177436947823, 0.2644347846508026, 1.0)

    colorramp_006_cre_1 = colorramp_006.color_ramp.elements.new(1.0)
    colorramp_006_cre_1.alpha = 1.0
    colorramp_006_cre_1.color = (0.0, 0.04002053663134575, 0.19306129217147827, 1.0)

    # node Brick Texture
    brick_texture = solarpanelshader.nodes.new("ShaderNodeTexBrick")
    brick_texture.name = "Brick Texture"
    brick_texture.offset = 0.0
    brick_texture.offset_frequency = 2
    brick_texture.squash = 1.0
    brick_texture.squash_frequency = 2
    # Color1
    brick_texture.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
    # Color2
    brick_texture.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
    # Mortar
    brick_texture.inputs[3].default_value = (1.0, 1.0, 1.0, 1.0)
    # Scale
    brick_texture.inputs[4].default_value = 5.0
    # Mortar Size
    brick_texture.inputs[5].default_value = 0.009999999776482582
    # Mortar Smooth
    brick_texture.inputs[6].default_value = 0.49000000953674316
    # Bias
    brick_texture.inputs[7].default_value = 0.0
    # Brick Width
    brick_texture.inputs[8].default_value = 0.625
    # Row Height
    brick_texture.inputs[9].default_value = 0.20000000298023224

    # node Mix.003
    mix_003 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = "LIGHTEN"
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = "RGBA"
    mix_003.factor_mode = "UNIFORM"
    # B_Color
    mix_003.inputs[7].default_value = (
        0.22322650253772736,
        0.22322815656661987,
        0.2232280671596527,
        1.0,
    )

    # node Mix.002
    mix_002 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = "MIX"
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = "RGBA"
    mix_002.factor_mode = "UNIFORM"
    # A_Color
    mix_002.inputs[6].default_value = (
        0.22322650253772736,
        0.22322815656661987,
        0.2232280671596527,
        1.0,
    )

    # node ColorRamp.003
    colorramp_003 = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp_003.name = "ColorRamp.003"
    colorramp_003.color_ramp.color_mode = "RGB"
    colorramp_003.color_ramp.hue_interpolation = "NEAR"
    colorramp_003.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_003.color_ramp.elements.remove(colorramp_003.color_ramp.elements[0])
    colorramp_003_cre_0 = colorramp_003.color_ramp.elements[0]
    colorramp_003_cre_0.position = 0.14025971293449402
    colorramp_003_cre_0.alpha = 1.0
    colorramp_003_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_003_cre_1 = colorramp_003.color_ramp.elements.new(0.8181816935539246)
    colorramp_003_cre_1.alpha = 1.0
    colorramp_003_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Reroute.002
    reroute_002 = solarpanelshader.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketVector"
    # node Texture Coordinate
    texture_coordinate = solarpanelshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    # node Mapping
    mapping = solarpanelshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = "POINT"
    # Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Value
    value = solarpanelshader.nodes.new("ShaderNodeValue")
    value.name = "Value"

    value.outputs[0].default_value = 3.5
    # node Mix.004
    mix_004 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.blend_type = "DARKEN"
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = "RGBA"
    mix_004.factor_mode = "UNIFORM"
    # B_Color
    mix_004.inputs[7].default_value = (
        0.00655383663251996,
        0.009497265331447124,
        0.024171071127057076,
        1.0,
    )

    # node Vector Math.001
    vector_math_001 = solarpanelshader.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = "MULTIPLY"
    # Vector_001
    vector_math_001.inputs[1].default_value = (1.0, 0.6399999856948853, 1.0)

    # node Group
    group = solarpanelshader.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = random_x4___mat
    # Socket_5
    group.inputs[0].default_value = 0.521340012550354

    # node Principled BSDF.001
    principled_bsdf_001 = solarpanelshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_001.name = "Principled BSDF.001"
    principled_bsdf_001.distribution = "MULTI_GGX"
    principled_bsdf_001.subsurface_method = "RANDOM_WALK"
    # Metallic
    principled_bsdf_001.inputs[1].default_value = 1.0
    # IOR
    principled_bsdf_001.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf_001.inputs[4].default_value = 1.0
    # Diffuse Roughness
    principled_bsdf_001.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf_001.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf_001.inputs[9].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf_001.inputs[10].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf_001.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf_001.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf_001.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf_001.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf_001.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf_001.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf_001.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf_001.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf_001.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf_001.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf_001.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf_001.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf_001.inputs[24].default_value = 0.0
    # Sheen Roughness
    principled_bsdf_001.inputs[25].default_value = 0.5
    # Sheen Tint
    principled_bsdf_001.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf_001.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf_001.inputs[28].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf_001.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf_001.inputs[30].default_value = 1.3300000429153442

    # node Map Range
    map_range = solarpanelshader.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = "FLOAT"
    map_range.interpolation_type = "LINEAR"
    # From Min
    map_range.inputs[1].default_value = 0.0
    # From Max
    map_range.inputs[2].default_value = 1.0
    # To Min
    map_range.inputs[3].default_value = 0.25
    # To Max
    map_range.inputs[4].default_value = 0.550000011920929

    # Set parents
    noise_texture.parent = frame_002
    mix_001.parent = frame_003
    bump_001.parent = frame_003
    colorramp_004.parent = frame_002
    reroute_001.parent = frame_002
    reroute.parent = frame_001
    colorramp_001.parent = frame
    voronoi_texture.parent = frame
    voronoi_texture_001.parent = frame
    colorramp.parent = frame
    vector_math.parent = frame
    mix.parent = frame
    voronoi_texture_002.parent = frame_001
    noise_texture_001.parent = frame_001
    colorramp_006.parent = frame_001
    brick_texture.parent = frame_001
    mix_003.parent = frame_001
    colorramp_003.parent = frame_001
    mix_004.parent = frame_001
    vector_math_001.parent = frame_001

    # Set locations
    group_output_1.location = (1357.573974609375, 281.4519958496094)
    frame_002.location = (502.4304504394531, -261.6494140625)
    frame_003.location = (264.04486083984375, 122.45939636230469)
    frame_001.location = (280.5555419921875, -20.9512939453125)
    frame.location = (242.02996826171875, -47.79149627685547)
    noise_texture.location = (-571.0491943359375, -530.0728759765625)
    mix_001.location = (335.08056640625, -152.2129669189453)
    bump_001.location = (527.4110717773438, -169.958984375)
    colorramp_004.location = (-354.1903076171875, -536.6217041015625)
    reroute_001.location = (-891.3917236328125, -639.0899047851562)
    reroute.location = (-813.19140625, 522.2021484375)
    colorramp_001.location = (-375.8592224121094, -148.3482208251953)
    voronoi_texture.location = (-549.3483276367188, 80.37715911865234)
    voronoi_texture_001.location = (-550.72802734375, -264.6904296875)
    colorramp.location = (-379.7568359375, 76.08872985839844)
    vector_math.location = (-734.3638305664062, -159.66159057617188)
    mix.location = (16.777664184570312, 10.651435852050781)
    voronoi_texture_002.location = (-680.0263671875, 497.43084716796875)
    noise_texture_001.location = (-676.8555297851562, 818.863525390625)
    colorramp_006.location = (-490.3884582519531, 539.2119140625)
    brick_texture.location = (-49.788970947265625, 533.8572998046875)
    mix_003.location = (246.53334045410156, 706.5650634765625)
    mix_002.location = (810.5228271484375, 304.9632263183594)
    colorramp_003.location = (-493.606201171875, 779.6920166015625)
    reroute_002.location = (-665.6483154296875, -141.8559112548828)
    texture_coordinate.location = (-1040.4798583984375, -104.36219024658203)
    mapping.location = (-854.9619140625, -109.00749206542969)
    value.location = (-1038.7108154296875, -353.26104736328125)
    mix_004.location = (-225.9229736328125, 734.1510620117188)
    vector_math_001.location = (-228.8770751953125, 434.66876220703125)
    group.location = (-1440.6337890625, -138.20118713378906)
    principled_bsdf_001.location = (1045.4649658203125, 280.4210205078125)
    map_range.location = (454.1365051269531, -315.53240966796875)

    # initialize solarpanelshader links
    # noise_texture.Fac -> colorramp_004.Fac
    solarpanelshader.links.new(noise_texture.outputs[0], colorramp_004.inputs[0])
    # texture_coordinate.Object -> mapping.Vector
    solarpanelshader.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    # voronoi_texture_001.Distance -> colorramp_001.Fac
    solarpanelshader.links.new(voronoi_texture_001.outputs[0], colorramp_001.inputs[0])
    # reroute.Output -> voronoi_texture_002.Vector
    solarpanelshader.links.new(reroute.outputs[0], voronoi_texture_002.inputs[0])
    # value.Value -> mapping.Scale
    solarpanelshader.links.new(value.outputs[0], mapping.inputs[3])
    # colorramp.Color -> mix.A
    solarpanelshader.links.new(colorramp.outputs[0], mix.inputs[6])
    # mix.Result -> mix_002.Factor
    solarpanelshader.links.new(mix.outputs[2], mix_002.inputs[0])
    # reroute.Output -> noise_texture_001.Vector
    solarpanelshader.links.new(reroute.outputs[0], noise_texture_001.inputs[0])
    # colorramp_001.Color -> mix.B
    solarpanelshader.links.new(colorramp_001.outputs[0], mix.inputs[7])
    # brick_texture.Color -> mix_003.Factor
    solarpanelshader.links.new(brick_texture.outputs[0], mix_003.inputs[0])
    # colorramp_003.Color -> mix_004.Factor
    solarpanelshader.links.new(colorramp_003.outputs[0], mix_004.inputs[0])
    # mix_003.Result -> mix_002.B
    solarpanelshader.links.new(mix_003.outputs[2], mix_002.inputs[7])
    # colorramp_006.Color -> mix_004.A
    solarpanelshader.links.new(colorramp_006.outputs[0], mix_004.inputs[6])
    # voronoi_texture_002.Color -> colorramp_006.Fac
    solarpanelshader.links.new(voronoi_texture_002.outputs[1], colorramp_006.inputs[0])
    # noise_texture_001.Fac -> colorramp_003.Fac
    solarpanelshader.links.new(noise_texture_001.outputs[0], colorramp_003.inputs[0])
    # vector_math_001.Vector -> brick_texture.Vector
    solarpanelshader.links.new(vector_math_001.outputs[0], brick_texture.inputs[0])
    # mix_004.Result -> mix_003.A
    solarpanelshader.links.new(mix_004.outputs[2], mix_003.inputs[6])
    # mapping.Vector -> reroute_002.Input
    solarpanelshader.links.new(mapping.outputs[0], reroute_002.inputs[0])
    # reroute_002.Output -> voronoi_texture.Vector
    solarpanelshader.links.new(reroute_002.outputs[0], voronoi_texture.inputs[0])
    # reroute_001.Output -> noise_texture.Vector
    solarpanelshader.links.new(reroute_001.outputs[0], noise_texture.inputs[0])
    # mix_001.Result -> bump_001.Height
    solarpanelshader.links.new(mix_001.outputs[2], bump_001.inputs[2])
    # vector_math.Vector -> voronoi_texture_001.Vector
    solarpanelshader.links.new(vector_math.outputs[0], voronoi_texture_001.inputs[0])
    # reroute_002.Output -> reroute.Input
    solarpanelshader.links.new(reroute_002.outputs[0], reroute.inputs[0])
    # brick_texture.Color -> mix_001.Factor
    solarpanelshader.links.new(brick_texture.outputs[0], mix_001.inputs[0])
    # voronoi_texture.Distance -> colorramp.Fac
    solarpanelshader.links.new(voronoi_texture.outputs[0], colorramp.inputs[0])
    # reroute_002.Output -> reroute_001.Input
    solarpanelshader.links.new(reroute_002.outputs[0], reroute_001.inputs[0])
    # mix.Result -> mix_001.A
    solarpanelshader.links.new(mix.outputs[2], mix_001.inputs[6])
    # reroute_002.Output -> vector_math.Vector
    solarpanelshader.links.new(reroute_002.outputs[0], vector_math.inputs[0])
    # reroute.Output -> vector_math_001.Vector
    solarpanelshader.links.new(reroute.outputs[0], vector_math_001.inputs[0])
    # group.0 -> noise_texture_001.W
    solarpanelshader.links.new(group.outputs[0], noise_texture_001.inputs[1])
    # group.1 -> voronoi_texture_002.W
    solarpanelshader.links.new(group.outputs[1], voronoi_texture_002.inputs[1])
    # principled_bsdf_001.BSDF -> group_output_1.BSDF
    solarpanelshader.links.new(principled_bsdf_001.outputs[0], group_output_1.inputs[0])
    # mix_002.Result -> principled_bsdf_001.Base Color
    solarpanelshader.links.new(mix_002.outputs[2], principled_bsdf_001.inputs[0])
    # colorramp_004.Color -> principled_bsdf_001.Roughness
    solarpanelshader.links.new(colorramp_004.outputs[0], principled_bsdf_001.inputs[2])
    # bump_001.Normal -> principled_bsdf_001.Normal
    solarpanelshader.links.new(bump_001.outputs[0], principled_bsdf_001.inputs[5])
    # group.2 -> noise_texture.W
    solarpanelshader.links.new(group.outputs[2], noise_texture.inputs[1])
    # group.3 -> map_range.Value
    solarpanelshader.links.new(group.outputs[3], map_range.inputs[0])
    # map_range.Result -> bump_001.Strength
    solarpanelshader.links.new(map_range.outputs[0], bump_001.inputs[0])
    return solarpanelshader


solarpanelshader = solarpanelshader_node_group()


# initialize SolarPanel node group
def solarpanel_node_group():
    solarpanel = mat.node_tree
    # start with a clean node tree
    for node in solarpanel.nodes:
        solarpanel.nodes.remove(node)
    solarpanel.color_tag = "NONE"
    solarpanel.description = ""
    solarpanel.default_group_node_width = 140

    # solarpanel interface

    # initialize solarpanel nodes
    # node Material Output
    material_output = solarpanel.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = "ALL"
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0

    # node Group
    group_1 = solarpanel.nodes.new("ShaderNodeGroup")
    group_1.name = "Group"
    group_1.node_tree = solarpanelshader

    # Set locations
    material_output.location = (1170.1507568359375, 376.55419921875)
    group_1.location = (796.747802734375, 443.9368896484375)

    # initialize solarpanel links
    # group_1.BSDF -> material_output.Surface
    solarpanel.links.new(group_1.outputs[0], material_output.inputs[0])
    return solarpanel


solarpanel = solarpanel_node_group()
