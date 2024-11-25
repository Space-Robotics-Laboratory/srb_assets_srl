import bpy
import mathutils

mat = bpy.data.materials.new(name="MartianSurface")
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


# initialize RockyGroundShader node group
def rockygroundshader_node_group():
    rockygroundshader = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="RockyGroundShader"
    )

    rockygroundshader.color_tag = "NONE"
    rockygroundshader.description = ""
    rockygroundshader.default_group_node_width = 140

    # rockygroundshader interface
    # Socket Shader
    shader_socket = rockygroundshader.interface.new_socket(
        name="Shader", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    shader_socket.attribute_domain = "POINT"

    # Socket Scale
    scale_socket = rockygroundshader.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e38
    scale_socket.max_value = 3.4028234663852886e38
    scale_socket.subtype = "NONE"
    scale_socket.attribute_domain = "POINT"

    # Socket Rocks Visibility
    rocks_visibility_socket = rockygroundshader.interface.new_socket(
        name="Rocks Visibility", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    rocks_visibility_socket.default_value = 1.0
    rocks_visibility_socket.min_value = 0.0
    rocks_visibility_socket.max_value = 2.0
    rocks_visibility_socket.subtype = "NONE"
    rocks_visibility_socket.attribute_domain = "POINT"

    # Socket Rock Color 1
    rock_color_1_socket = rockygroundshader.interface.new_socket(
        name="Rock Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    rock_color_1_socket.default_value = (
        0.10047899931669235,
        0.10047899931669235,
        0.10047899931669235,
        1.0,
    )
    rock_color_1_socket.attribute_domain = "POINT"

    # Socket Rock Color 2
    rock_color_2_socket = rockygroundshader.interface.new_socket(
        name="Rock Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    rock_color_2_socket.default_value = (
        0.10048799961805344,
        0.08293099701404572,
        0.07997799664735794,
        1.0,
    )
    rock_color_2_socket.attribute_domain = "POINT"

    # Socket Rocks Detail
    rocks_detail_socket = rockygroundshader.interface.new_socket(
        name="Rocks Detail", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    rocks_detail_socket.default_value = 0.5
    rocks_detail_socket.min_value = 0.0
    rocks_detail_socket.max_value = 1.0
    rocks_detail_socket.subtype = "FACTOR"
    rocks_detail_socket.attribute_domain = "POINT"

    # Socket Large Rocks Scale
    large_rocks_scale_socket = rockygroundshader.interface.new_socket(
        name="Large Rocks Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    large_rocks_scale_socket.default_value = 14.0
    large_rocks_scale_socket.min_value = -1000.0
    large_rocks_scale_socket.max_value = 1000.0
    large_rocks_scale_socket.subtype = "NONE"
    large_rocks_scale_socket.attribute_domain = "POINT"

    # Socket Small Rocks Scale
    small_rocks_scale_socket = rockygroundshader.interface.new_socket(
        name="Small Rocks Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    small_rocks_scale_socket.default_value = 34.0
    small_rocks_scale_socket.min_value = -1000.0
    small_rocks_scale_socket.max_value = 1000.0
    small_rocks_scale_socket.subtype = "NONE"
    small_rocks_scale_socket.attribute_domain = "POINT"

    # Socket Dirt Color 1
    dirt_color_1_socket = rockygroundshader.interface.new_socket(
        name="Dirt Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    dirt_color_1_socket.default_value = (
        0.12273299694061279,
        0.06268499791622162,
        0.028358999639749527,
        1.0,
    )
    dirt_color_1_socket.attribute_domain = "POINT"

    # Socket Dirt Color 2
    dirt_color_2_socket = rockygroundshader.interface.new_socket(
        name="Dirt Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    dirt_color_2_socket.default_value = (
        0.016374999657273293,
        0.011485000140964985,
        0.006409999914467335,
        1.0,
    )
    dirt_color_2_socket.attribute_domain = "POINT"

    # Socket Dirt Color 3
    dirt_color_3_socket = rockygroundshader.interface.new_socket(
        name="Dirt Color 3", in_out="INPUT", socket_type="NodeSocketColor"
    )
    dirt_color_3_socket.default_value = (
        0.01637599989771843,
        0.012590999715030193,
        0.00964600034058094,
        1.0,
    )
    dirt_color_3_socket.attribute_domain = "POINT"

    # Socket Roughness
    roughness_socket = rockygroundshader.interface.new_socket(
        name="Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = "NONE"
    roughness_socket.attribute_domain = "POINT"

    # Socket Dirt Bump Strength
    dirt_bump_strength_socket = rockygroundshader.interface.new_socket(
        name="Dirt Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    dirt_bump_strength_socket.default_value = 0.15000000596046448
    dirt_bump_strength_socket.min_value = 0.0
    dirt_bump_strength_socket.max_value = 1.0
    dirt_bump_strength_socket.subtype = "FACTOR"
    dirt_bump_strength_socket.attribute_domain = "POINT"

    # Socket Rock Bump Strength
    rock_bump_strength_socket = rockygroundshader.interface.new_socket(
        name="Rock Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    rock_bump_strength_socket.default_value = 0.5
    rock_bump_strength_socket.min_value = 0.0
    rock_bump_strength_socket.max_value = 1.0
    rock_bump_strength_socket.subtype = "FACTOR"
    rock_bump_strength_socket.attribute_domain = "POINT"

    # Socket Extra Bump Strength
    extra_bump_strength_socket = rockygroundshader.interface.new_socket(
        name="Extra Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    extra_bump_strength_socket.default_value = 0.05999999865889549
    extra_bump_strength_socket.min_value = 0.0
    extra_bump_strength_socket.max_value = 1000.0
    extra_bump_strength_socket.subtype = "NONE"
    extra_bump_strength_socket.attribute_domain = "POINT"

    # initialize rockygroundshader nodes
    # node Frame.001
    frame_001 = rockygroundshader.nodes.new("NodeFrame")
    frame_001.label = "Large Rocks"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # node Frame.002
    frame_002 = rockygroundshader.nodes.new("NodeFrame")
    frame_002.label = "Small Rocks"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # node Frame.004
    frame_004 = rockygroundshader.nodes.new("NodeFrame")
    frame_004.label = "Rock Color"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    # node Frame.003
    frame_003 = rockygroundshader.nodes.new("NodeFrame")
    frame_003.label = "Dirt Color"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # node Frame.006
    frame_006 = rockygroundshader.nodes.new("NodeFrame")
    frame_006.label = "Base Color"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    # node Frame.005
    frame_005 = rockygroundshader.nodes.new("NodeFrame")
    frame_005.label = "Dirt"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # node Frame.009
    frame_009 = rockygroundshader.nodes.new("NodeFrame")
    frame_009.label = "Bump"
    frame_009.name = "Frame.009"
    frame_009.label_size = 20
    frame_009.shrink = True

    # node Frame
    frame = rockygroundshader.nodes.new("NodeFrame")
    frame.label = "Mapping"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # node Frame.008
    frame_008 = rockygroundshader.nodes.new("NodeFrame")
    frame_008.label = "Roughness"
    frame_008.name = "Frame.008"
    frame_008.label_size = 20
    frame_008.shrink = True

    # node Group Output
    group_output_1 = rockygroundshader.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # node Color Ramp
    color_ramp = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = "RGB"
    color_ramp.color_ramp.hue_interpolation = "NEAR"
    color_ramp.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.06783919036388397
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(1.0)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Noise Texture
    noise_texture = rockygroundshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = "3D"
    noise_texture.noise_type = "FBM"
    noise_texture.normalize = True
    # Scale
    noise_texture.inputs[2].default_value = 0.30000001192092896
    # Detail
    noise_texture.inputs[3].default_value = 15.0
    # Roughness
    noise_texture.inputs[4].default_value = 0.550000011920929
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.4000000953674316
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # node Noise Texture.001
    noise_texture_001 = rockygroundshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = "3D"
    noise_texture_001.noise_type = "FBM"
    noise_texture_001.normalize = True
    # Scale
    noise_texture_001.inputs[2].default_value = 8.0
    # Detail
    noise_texture_001.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_001.inputs[4].default_value = 0.33000001311302185
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 2.4000000953674316
    # Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    # node Color Ramp.001
    color_ramp_001 = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.name = "Color Ramp.001"
    color_ramp_001.color_ramp.color_mode = "RGB"
    color_ramp_001.color_ramp.hue_interpolation = "NEAR"
    color_ramp_001.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
    color_ramp_001_cre_0.position = 0.4547737240791321
    color_ramp_001_cre_0.alpha = 1.0
    color_ramp_001_cre_0.color = (1.0, 1.0, 1.0, 1.0)

    color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.5804020762443542)
    color_ramp_001_cre_1.alpha = 1.0
    color_ramp_001_cre_1.color = (0.0, 0.0, 0.0, 1.0)

    # node Color Ramp.003
    color_ramp_003 = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_003.name = "Color Ramp.003"
    color_ramp_003.color_ramp.color_mode = "RGB"
    color_ramp_003.color_ramp.hue_interpolation = "NEAR"
    color_ramp_003.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_003.color_ramp.elements.remove(color_ramp_003.color_ramp.elements[0])
    color_ramp_003_cre_0 = color_ramp_003.color_ramp.elements[0]
    color_ramp_003_cre_0.position = 0.4547737240791321
    color_ramp_003_cre_0.alpha = 1.0
    color_ramp_003_cre_0.color = (1.0, 1.0, 1.0, 1.0)

    color_ramp_003_cre_1 = color_ramp_003.color_ramp.elements.new(0.5804020762443542)
    color_ramp_003_cre_1.alpha = 1.0
    color_ramp_003_cre_1.color = (0.0, 0.0, 0.0, 1.0)

    # node Noise Texture.002
    noise_texture_002 = rockygroundshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_002.name = "Noise Texture.002"
    noise_texture_002.noise_dimensions = "3D"
    noise_texture_002.noise_type = "FBM"
    noise_texture_002.normalize = True
    # Scale
    noise_texture_002.inputs[2].default_value = 0.8999999761581421
    # Detail
    noise_texture_002.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_002.inputs[4].default_value = 0.550000011920929
    # Lacunarity
    noise_texture_002.inputs[5].default_value = 2.4000000953674316
    # Distortion
    noise_texture_002.inputs[8].default_value = 0.0

    # node Mix.002
    mix_002 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = "LINEAR_LIGHT"
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = "RGBA"
    mix_002.factor_mode = "UNIFORM"
    # Factor_Float
    mix_002.inputs[0].default_value = 0.30000001192092896

    # node Noise Texture.003
    noise_texture_003 = rockygroundshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003.name = "Noise Texture.003"
    noise_texture_003.noise_dimensions = "3D"
    noise_texture_003.noise_type = "FBM"
    noise_texture_003.normalize = True
    # Scale
    noise_texture_003.inputs[2].default_value = 17.0
    # Detail
    noise_texture_003.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_003.inputs[4].default_value = 0.33000001311302185
    # Lacunarity
    noise_texture_003.inputs[5].default_value = 2.4000000953674316
    # Distortion
    noise_texture_003.inputs[8].default_value = 0.0

    # node Color Ramp.002
    color_ramp_002 = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_002.name = "Color Ramp.002"
    color_ramp_002.color_ramp.color_mode = "RGB"
    color_ramp_002.color_ramp.hue_interpolation = "NEAR"
    color_ramp_002.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_002.color_ramp.elements.remove(color_ramp_002.color_ramp.elements[0])
    color_ramp_002_cre_0 = color_ramp_002.color_ramp.elements[0]
    color_ramp_002_cre_0.position = 0.19346728920936584
    color_ramp_002_cre_0.alpha = 1.0
    color_ramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_002_cre_1 = color_ramp_002.color_ramp.elements.new(0.5854271054267883)
    color_ramp_002_cre_1.alpha = 1.0
    color_ramp_002_cre_1.color = (
        0.17047399282455444,
        0.17047399282455444,
        0.17047399282455444,
        1.0,
    )

    # node Mix.001
    mix_001 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = "MIX"
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = "RGBA"
    mix_001.factor_mode = "UNIFORM"
    # B_Color
    mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)

    # node Mix.003
    mix_003 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = "MIX"
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = "RGBA"
    mix_003.factor_mode = "UNIFORM"
    # B_Color
    mix_003.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)

    # node Noise Texture.005
    noise_texture_005 = rockygroundshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_005.name = "Noise Texture.005"
    noise_texture_005.noise_dimensions = "3D"
    noise_texture_005.noise_type = "FBM"
    noise_texture_005.normalize = True
    # Scale
    noise_texture_005.inputs[2].default_value = 13.0
    # Detail
    noise_texture_005.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_005.inputs[4].default_value = 0.699999988079071
    # Lacunarity
    noise_texture_005.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_005.inputs[8].default_value = 0.0

    # node Noise Texture.004
    noise_texture_004 = rockygroundshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_004.name = "Noise Texture.004"
    noise_texture_004.noise_dimensions = "3D"
    noise_texture_004.noise_type = "FBM"
    noise_texture_004.normalize = True
    # Scale
    noise_texture_004.inputs[2].default_value = 8.699999809265137
    # Detail
    noise_texture_004.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_004.inputs[4].default_value = 0.6200000047683716
    # Lacunarity
    noise_texture_004.inputs[5].default_value = 3.5999999046325684
    # Distortion
    noise_texture_004.inputs[8].default_value = 0.0

    # node Color Ramp.004
    color_ramp_004 = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = "RGB"
    color_ramp_004.color_ramp.hue_interpolation = "NEAR"
    color_ramp_004.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.31407034397125244
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(0.6834171414375305)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Color Ramp.005
    color_ramp_005 = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = "RGB"
    color_ramp_005.color_ramp.hue_interpolation = "NEAR"
    color_ramp_005.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.0
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (
        0.10046599805355072,
        0.10046599805355072,
        0.10046599805355072,
        1.0,
    )

    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.497487336397171)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (
        0.031199999153614044,
        0.031199999153614044,
        0.031199999153614044,
        1.0,
    )

    color_ramp_005_cre_2 = color_ramp_005.color_ramp.elements.new(1.0)
    color_ramp_005_cre_2.alpha = 1.0
    color_ramp_005_cre_2.color = (
        0.4479770064353943,
        0.4479770064353943,
        0.4479770064353943,
        1.0,
    )

    # node Voronoi Texture.002
    voronoi_texture_002 = rockygroundshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_002.name = "Voronoi Texture.002"
    voronoi_texture_002.distance = "EUCLIDEAN"
    voronoi_texture_002.feature = "SMOOTH_F1"
    voronoi_texture_002.normalize = False
    voronoi_texture_002.voronoi_dimensions = "3D"
    # Scale
    voronoi_texture_002.inputs[2].default_value = 5.0
    # Detail
    voronoi_texture_002.inputs[3].default_value = 15.0
    # Roughness
    voronoi_texture_002.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture_002.inputs[5].default_value = 6.400000095367432
    # Smoothness
    voronoi_texture_002.inputs[6].default_value = 1.0
    # Randomness
    voronoi_texture_002.inputs[8].default_value = 1.0

    # node Mix.008
    mix_008 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_008.name = "Mix.008"
    mix_008.blend_type = "MIX"
    mix_008.clamp_factor = True
    mix_008.clamp_result = False
    mix_008.data_type = "RGBA"
    mix_008.factor_mode = "UNIFORM"

    # node Noise Texture.007
    noise_texture_007 = rockygroundshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_007.name = "Noise Texture.007"
    noise_texture_007.noise_dimensions = "3D"
    noise_texture_007.noise_type = "FBM"
    noise_texture_007.normalize = True
    # Scale
    noise_texture_007.inputs[2].default_value = 35.0
    # Detail
    noise_texture_007.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_007.inputs[4].default_value = 0.699999988079071
    # Lacunarity
    noise_texture_007.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_007.inputs[8].default_value = 0.0

    # node Color Ramp.006
    color_ramp_006 = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006.name = "Color Ramp.006"
    color_ramp_006.color_ramp.color_mode = "RGB"
    color_ramp_006.color_ramp.hue_interpolation = "NEAR"
    color_ramp_006.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_006.color_ramp.elements.remove(color_ramp_006.color_ramp.elements[0])
    color_ramp_006_cre_0 = color_ramp_006.color_ramp.elements[0]
    color_ramp_006_cre_0.position = 0.359296590089798
    color_ramp_006_cre_0.alpha = 1.0
    color_ramp_006_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_006_cre_1 = color_ramp_006.color_ramp.elements.new(0.7638190984725952)
    color_ramp_006_cre_1.alpha = 1.0
    color_ramp_006_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Color Ramp.007
    color_ramp_007 = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_007.name = "Color Ramp.007"
    color_ramp_007.color_ramp.color_mode = "RGB"
    color_ramp_007.color_ramp.hue_interpolation = "NEAR"
    color_ramp_007.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_007.color_ramp.elements.remove(color_ramp_007.color_ramp.elements[0])
    color_ramp_007_cre_0 = color_ramp_007.color_ramp.elements[0]
    color_ramp_007_cre_0.position = 0.0
    color_ramp_007_cre_0.alpha = 1.0
    color_ramp_007_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_007_cre_1 = color_ramp_007.color_ramp.elements.new(0.06281421333551407)
    color_ramp_007_cre_1.alpha = 1.0
    color_ramp_007_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Mix.009
    mix_009 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_009.name = "Mix.009"
    mix_009.blend_type = "LIGHTEN"
    mix_009.clamp_factor = True
    mix_009.clamp_result = False
    mix_009.data_type = "RGBA"
    mix_009.factor_mode = "UNIFORM"
    # Factor_Float
    mix_009.inputs[0].default_value = 0.15000000596046448

    # node Math
    math_1 = rockygroundshader.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = "ADD"
    math_1.use_clamp = False
    # Value_001
    math_1.inputs[1].default_value = 0.5

    # node Principled BSDF
    principled_bsdf = rockygroundshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = "MULTI_GGX"
    principled_bsdf.subsurface_method = "RANDOM_WALK"
    # Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    # IOR
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
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

    # node Noise Texture.006
    noise_texture_006 = rockygroundshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_006.name = "Noise Texture.006"
    noise_texture_006.noise_dimensions = "3D"
    noise_texture_006.noise_type = "FBM"
    noise_texture_006.normalize = True
    # Scale
    noise_texture_006.inputs[2].default_value = 18.0
    # Detail
    noise_texture_006.inputs[3].default_value = 15.0
    # Lacunarity
    noise_texture_006.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_006.inputs[8].default_value = 0.0

    # node Texture Coordinate
    texture_coordinate = rockygroundshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    # node Mapping
    mapping = rockygroundshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = "POINT"
    # Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Mix.004
    mix_004 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.blend_type = "LIGHTEN"
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = "RGBA"
    mix_004.factor_mode = "UNIFORM"
    # Factor_Float
    mix_004.inputs[0].default_value = 1.0

    # node Hue/Saturation/Value.001
    hue_saturation_value_001 = rockygroundshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_001.name = "Hue/Saturation/Value.001"
    # Hue
    hue_saturation_value_001.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value_001.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value_001.inputs[3].default_value = 1.0

    # node Hue/Saturation/Value.002
    hue_saturation_value_002 = rockygroundshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_002.name = "Hue/Saturation/Value.002"
    # Hue
    hue_saturation_value_002.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value_002.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value_002.inputs[3].default_value = 1.0

    # node Mix.007
    mix_007 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_007.name = "Mix.007"
    mix_007.blend_type = "MIX"
    mix_007.clamp_factor = True
    mix_007.clamp_result = False
    mix_007.data_type = "RGBA"
    mix_007.factor_mode = "UNIFORM"

    # node Mix
    mix = rockygroundshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = "LINEAR_LIGHT"
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = "RGBA"
    mix.factor_mode = "UNIFORM"

    # node Voronoi Texture
    voronoi_texture = rockygroundshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = "EUCLIDEAN"
    voronoi_texture.feature = "DISTANCE_TO_EDGE"
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = "3D"
    # Detail
    voronoi_texture.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture.inputs[8].default_value = 1.0

    # node Voronoi Texture.001
    voronoi_texture_001 = rockygroundshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = "EUCLIDEAN"
    voronoi_texture_001.feature = "DISTANCE_TO_EDGE"
    voronoi_texture_001.normalize = False
    voronoi_texture_001.voronoi_dimensions = "3D"
    # Detail
    voronoi_texture_001.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_001.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture_001.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture_001.inputs[8].default_value = 1.0

    # node Mix.005
    mix_005 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_005.name = "Mix.005"
    mix_005.blend_type = "MIX"
    mix_005.clamp_factor = True
    mix_005.clamp_result = False
    mix_005.data_type = "RGBA"
    mix_005.factor_mode = "UNIFORM"

    # node Mix.006
    mix_006 = rockygroundshader.nodes.new("ShaderNodeMix")
    mix_006.name = "Mix.006"
    mix_006.blend_type = "MIX"
    mix_006.clamp_factor = True
    mix_006.clamp_result = False
    mix_006.data_type = "RGBA"
    mix_006.factor_mode = "UNIFORM"

    # node Color Ramp.008
    color_ramp_008 = rockygroundshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_008.name = "Color Ramp.008"
    color_ramp_008.color_ramp.color_mode = "RGB"
    color_ramp_008.color_ramp.hue_interpolation = "NEAR"
    color_ramp_008.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_008.color_ramp.elements.remove(color_ramp_008.color_ramp.elements[0])
    color_ramp_008_cre_0 = color_ramp_008.color_ramp.elements[0]
    color_ramp_008_cre_0.position = 0.0
    color_ramp_008_cre_0.alpha = 1.0
    color_ramp_008_cre_0.color = (
        0.7721049785614014,
        0.7721049785614014,
        0.7721049785614014,
        1.0,
    )

    color_ramp_008_cre_1 = color_ramp_008.color_ramp.elements.new(0.1356785148382187)
    color_ramp_008_cre_1.alpha = 1.0
    color_ramp_008_cre_1.color = (
        0.6128469705581665,
        0.6128469705581665,
        0.6128469705581665,
        1.0,
    )

    # node Hue/Saturation/Value
    hue_saturation_value = rockygroundshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    # Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    # node Bump
    bump = rockygroundshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    # Distance
    bump.inputs[1].default_value = 1.0

    # node Bump.002
    bump_002 = rockygroundshader.nodes.new("ShaderNodeBump")
    bump_002.name = "Bump.002"
    bump_002.invert = False
    # Distance
    bump_002.inputs[1].default_value = 1.0

    # node Bump.001
    bump_001 = rockygroundshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    # Distance
    bump_001.inputs[1].default_value = 1.0

    # node Group Input
    group_input_1 = rockygroundshader.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    # node Clamp
    clamp = rockygroundshader.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.hide = True
    clamp.clamp_type = "MINMAX"
    # Min
    clamp.inputs[1].default_value = 0.0
    # Max
    clamp.inputs[2].default_value = 1.0

    # node Bump.003
    bump_003 = rockygroundshader.nodes.new("ShaderNodeBump")
    bump_003.name = "Bump.003"
    bump_003.invert = False
    # Distance
    bump_003.inputs[1].default_value = 1.0
    # Normal
    bump_003.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Group.001
    group_001 = rockygroundshader.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random_x4___mat
    # Socket_5
    group_001.inputs[0].default_value = 0.5231512188911438

    # node Map Range.004
    map_range_004 = rockygroundshader.nodes.new("ShaderNodeMapRange")
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

    # Set parents
    color_ramp.parent = frame_001
    noise_texture.parent = frame_001
    noise_texture_001.parent = frame_001
    color_ramp_001.parent = frame_001
    color_ramp_003.parent = frame_002
    noise_texture_002.parent = frame_002
    mix_002.parent = frame_002
    noise_texture_003.parent = frame_002
    color_ramp_002.parent = frame_002
    mix_001.parent = frame_001
    mix_003.parent = frame_002
    noise_texture_005.parent = frame_004
    noise_texture_004.parent = frame_003
    color_ramp_004.parent = frame_003
    color_ramp_005.parent = frame_003
    voronoi_texture_002.parent = frame_003
    mix_008.parent = frame_006
    noise_texture_007.parent = frame_005
    color_ramp_006.parent = frame_005
    color_ramp_007.parent = frame_006
    noise_texture_006.parent = frame_005
    texture_coordinate.parent = frame
    mapping.parent = frame
    mix_007.parent = frame_004
    mix.parent = frame_001
    voronoi_texture.parent = frame_001
    voronoi_texture_001.parent = frame_002
    mix_005.parent = frame_003
    mix_006.parent = frame_003
    color_ramp_008.parent = frame_008
    hue_saturation_value.parent = frame_008
    bump.parent = frame_009
    bump_002.parent = frame_009
    bump_001.parent = frame_009
    clamp.parent = frame_005
    bump_003.parent = frame_009

    # Set locations
    frame_001.location = (9.24249267578125, -1082.150390625)
    frame_002.location = (-8.91021728515625, -430.821044921875)
    frame_004.location = (58.07061767578125, -1027.0340576171875)
    frame_003.location = (56.129150390625, -1020.23779296875)
    frame_006.location = (253.4292755126953, -1027.0340576171875)
    frame_005.location = (58.07061767578125, -1027.0340576171875)
    frame_009.location = (251.6049346923828, -1023.3848266601562)
    frame.location = (-693.2164916992188, -434.13116455078125)
    frame_008.location = (231.24842834472656, -937.7694702148438)
    group_output_1.location = (1978.334228515625, 0.0)
    color_ramp.location = (-305.6305236816406, 297.1470031738281)
    noise_texture.location = (-779.2238159179688, 277.68695068359375)
    noise_texture_001.location = (-771.6538696289062, 552.0715942382812)
    color_ramp_001.location = (-357.3363037109375, 517.9135131835938)
    color_ramp_003.location = (-357.3363037109375, 517.9135131835938)
    noise_texture_002.location = (-779.2238159179688, 277.68695068359375)
    mix_002.location = (-614.3984375, 257.658447265625)
    noise_texture_003.location = (-771.6538696289062, 552.0715942382812)
    color_ramp_002.location = (-305.6305236816406, 297.1470031738281)
    mix_001.location = (-44.38520812988281, 452.5235900878906)
    mix_003.location = (-44.38520812988281, 452.5235900878906)
    noise_texture_005.location = (-776.3880615234375, 2177.888916015625)
    noise_texture_004.location = (-800.2752685546875, 1473.79736328125)
    color_ramp_004.location = (-581.5419921875, 1467.8177490234375)
    color_ramp_005.location = (-558.1763916015625, 1718.25341796875)
    voronoi_texture_002.location = (-795.1177978515625, 1829.00439453125)
    mix_008.location = (633.4256591796875, 905.8595581054688)
    noise_texture_007.location = (-780.698974609375, -159.2308349609375)
    color_ramp_006.location = (-559.0987548828125, -163.19346618652344)
    color_ramp_007.location = (345.871337890625, 901.5951538085938)
    mix_009.location = (456.9305725097656, -619.0070190429688)
    math_1.location = (686.5902099609375, -615.3849487304688)
    principled_bsdf.location = (1688.334228515625, -135.0859375)
    noise_texture_006.location = (-227.2909393310547, -153.17327880859375)
    texture_coordinate.location = (-770.4983520507812, 276.35455322265625)
    mapping.location = (-595.4342041015625, 266.1795654296875)
    mix_004.location = (417.1983947753906, -382.135986328125)
    hue_saturation_value_001.location = (181.7850799560547, -205.70558166503906)
    hue_saturation_value_002.location = (188.97032165527344, -575.7411499023438)
    mix_007.location = (-269.95465087890625, 2163.447998046875)
    mix.location = (-614.3984375, 257.658447265625)
    voronoi_texture.location = (-460.01947021484375, 286.8158874511719)
    voronoi_texture_001.location = (-460.01947021484375, 286.8158874511719)
    mix_005.location = (-322.1456298828125, 1490.758056640625)
    mix_006.location = (-171.7185516357422, 1669.7777099609375)
    color_ramp_008.location = (904.6746826171875, 794.8360595703125)
    hue_saturation_value.location = (1164.760986328125, 780.5885009765625)
    bump.location = (828.0635986328125, 583.2872314453125)
    bump_002.location = (1160.1448974609375, 590.1194458007812)
    bump_001.location = (994.9806518554688, 587.3065185546875)
    group_input_1.location = (-1464.8040771484375, -488.8551330566406)
    clamp.location = (-227.2909393310547, -453.17327880859375)
    bump_003.location = (644.2456665039062, 572.53515625)
    group_001.location = (-1826.25048828125, -94.89218139648438)
    map_range_004.location = (-1657.435302734375, -329.9584045410156)

    # initialize rockygroundshader links
    # color_ramp_002.Color -> mix_003.A
    rockygroundshader.links.new(color_ramp_002.outputs[0], mix_003.inputs[6])
    # mapping.Vector -> mix_002.A
    rockygroundshader.links.new(mapping.outputs[0], mix_002.inputs[6])
    # hue_saturation_value_001.Color -> mix_004.B
    rockygroundshader.links.new(hue_saturation_value_001.outputs[0], mix_004.inputs[7])
    # hue_saturation_value_002.Color -> mix_004.A
    rockygroundshader.links.new(hue_saturation_value_002.outputs[0], mix_004.inputs[6])
    # mapping.Vector -> noise_texture_004.Vector
    rockygroundshader.links.new(mapping.outputs[0], noise_texture_004.inputs[0])
    # noise_texture_004.Fac -> color_ramp_004.Fac
    rockygroundshader.links.new(noise_texture_004.outputs[0], color_ramp_004.inputs[0])
    # mix_004.Result -> color_ramp_007.Fac
    rockygroundshader.links.new(mix_004.outputs[2], color_ramp_007.inputs[0])
    # color_ramp_004.Color -> mix_005.Factor
    rockygroundshader.links.new(color_ramp_004.outputs[0], mix_005.inputs[0])
    # mapping.Vector -> voronoi_texture_002.Vector
    rockygroundshader.links.new(mapping.outputs[0], voronoi_texture_002.inputs[0])
    # mix_004.Result -> bump_001.Height
    rockygroundshader.links.new(mix_004.outputs[2], bump_001.inputs[2])
    # voronoi_texture_002.Distance -> color_ramp_005.Fac
    rockygroundshader.links.new(
        voronoi_texture_002.outputs[0], color_ramp_005.inputs[0]
    )
    # mapping.Vector -> noise_texture_002.Vector
    rockygroundshader.links.new(mapping.outputs[0], noise_texture_002.inputs[0])
    # color_ramp_005.Color -> mix_006.Factor
    rockygroundshader.links.new(color_ramp_005.outputs[0], mix_006.inputs[0])
    # mapping.Vector -> noise_texture_001.Vector
    rockygroundshader.links.new(mapping.outputs[0], noise_texture_001.inputs[0])
    # mix_005.Result -> mix_006.A
    rockygroundshader.links.new(mix_005.outputs[2], mix_006.inputs[6])
    # mapping.Vector -> noise_texture_005.Vector
    rockygroundshader.links.new(mapping.outputs[0], noise_texture_005.inputs[0])
    # noise_texture_005.Fac -> mix_007.Factor
    rockygroundshader.links.new(noise_texture_005.outputs[0], mix_007.inputs[0])
    # mapping.Vector -> noise_texture_003.Vector
    rockygroundshader.links.new(mapping.outputs[0], noise_texture_003.inputs[0])
    # mapping.Vector -> noise_texture_006.Vector
    rockygroundshader.links.new(mapping.outputs[0], noise_texture_006.inputs[0])
    # mapping.Vector -> noise_texture_007.Vector
    rockygroundshader.links.new(mapping.outputs[0], noise_texture_007.inputs[0])
    # mix.Result -> voronoi_texture.Vector
    rockygroundshader.links.new(mix.outputs[2], voronoi_texture.inputs[0])
    # bump_001.Normal -> bump_002.Normal
    rockygroundshader.links.new(bump_001.outputs[0], bump_002.inputs[3])
    # mix_004.Result -> mix_009.A
    rockygroundshader.links.new(mix_004.outputs[2], mix_009.inputs[6])
    # noise_texture_007.Fac -> color_ramp_006.Fac
    rockygroundshader.links.new(noise_texture_007.outputs[0], color_ramp_006.inputs[0])
    # texture_coordinate.Object -> mapping.Vector
    rockygroundshader.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    # color_ramp_007.Color -> mix_008.Factor
    rockygroundshader.links.new(color_ramp_007.outputs[0], mix_008.inputs[0])
    # bump.Normal -> bump_001.Normal
    rockygroundshader.links.new(bump.outputs[0], bump_001.inputs[3])
    # mix_007.Result -> mix_008.B
    rockygroundshader.links.new(mix_007.outputs[2], mix_008.inputs[7])
    # noise_texture.Color -> mix.B
    rockygroundshader.links.new(noise_texture.outputs[1], mix.inputs[7])
    # voronoi_texture_001.Distance -> color_ramp_002.Fac
    rockygroundshader.links.new(
        voronoi_texture_001.outputs[0], color_ramp_002.inputs[0]
    )
    # voronoi_texture.Distance -> color_ramp.Fac
    rockygroundshader.links.new(voronoi_texture.outputs[0], color_ramp.inputs[0])
    # noise_texture_006.Fac -> mix_009.B
    rockygroundshader.links.new(noise_texture_006.outputs[0], mix_009.inputs[7])
    # mix_008.Result -> principled_bsdf.Base Color
    rockygroundshader.links.new(mix_008.outputs[2], principled_bsdf.inputs[0])
    # mapping.Vector -> noise_texture.Vector
    rockygroundshader.links.new(mapping.outputs[0], noise_texture.inputs[0])
    # noise_texture_006.Fac -> bump_002.Height
    rockygroundshader.links.new(noise_texture_006.outputs[0], bump_002.inputs[2])
    # noise_texture_001.Fac -> color_ramp_001.Fac
    rockygroundshader.links.new(noise_texture_001.outputs[0], color_ramp_001.inputs[0])
    # color_ramp_001.Color -> mix_001.Factor
    rockygroundshader.links.new(color_ramp_001.outputs[0], mix_001.inputs[0])
    # color_ramp.Color -> mix_001.A
    rockygroundshader.links.new(color_ramp.outputs[0], mix_001.inputs[6])
    # mix_009.Result -> math_1.Value
    rockygroundshader.links.new(mix_009.outputs[2], math_1.inputs[0])
    # mapping.Vector -> mix.A
    rockygroundshader.links.new(mapping.outputs[0], mix.inputs[6])
    # hue_saturation_value.Color -> principled_bsdf.Roughness
    rockygroundshader.links.new(
        hue_saturation_value.outputs[0], principled_bsdf.inputs[2]
    )
    # noise_texture_002.Color -> mix_002.B
    rockygroundshader.links.new(noise_texture_002.outputs[1], mix_002.inputs[7])
    # bump_002.Normal -> principled_bsdf.Normal
    rockygroundshader.links.new(bump_002.outputs[0], principled_bsdf.inputs[5])
    # color_ramp_008.Color -> hue_saturation_value.Color
    rockygroundshader.links.new(
        color_ramp_008.outputs[0], hue_saturation_value.inputs[4]
    )
    # color_ramp_007.Color -> color_ramp_008.Fac
    rockygroundshader.links.new(color_ramp_007.outputs[0], color_ramp_008.inputs[0])
    # mix_006.Result -> bump.Height
    rockygroundshader.links.new(mix_006.outputs[2], bump.inputs[2])
    # mix_002.Result -> voronoi_texture_001.Vector
    rockygroundshader.links.new(mix_002.outputs[2], voronoi_texture_001.inputs[0])
    # noise_texture_003.Fac -> color_ramp_003.Fac
    rockygroundshader.links.new(noise_texture_003.outputs[0], color_ramp_003.inputs[0])
    # color_ramp_003.Color -> mix_003.Factor
    rockygroundshader.links.new(color_ramp_003.outputs[0], mix_003.inputs[0])
    # mix_006.Result -> mix_008.A
    rockygroundshader.links.new(mix_006.outputs[2], mix_008.inputs[6])
    # principled_bsdf.BSDF -> group_output_1.Shader
    rockygroundshader.links.new(principled_bsdf.outputs[0], group_output_1.inputs[0])
    # group_input_1.Scale -> mapping.Scale
    rockygroundshader.links.new(group_input_1.outputs[0], mapping.inputs[3])
    # mix_003.Result -> hue_saturation_value_001.Color
    rockygroundshader.links.new(mix_003.outputs[2], hue_saturation_value_001.inputs[4])
    # mix_001.Result -> hue_saturation_value_002.Color
    rockygroundshader.links.new(mix_001.outputs[2], hue_saturation_value_002.inputs[4])
    # group_input_1.Rocks Visibility -> hue_saturation_value_002.Value
    rockygroundshader.links.new(
        group_input_1.outputs[1], hue_saturation_value_002.inputs[2]
    )
    # group_input_1.Rocks Visibility -> hue_saturation_value_001.Value
    rockygroundshader.links.new(
        group_input_1.outputs[1], hue_saturation_value_001.inputs[2]
    )
    # group_input_1.Rock Color 1 -> mix_007.A
    rockygroundshader.links.new(group_input_1.outputs[2], mix_007.inputs[6])
    # group_input_1.Rock Color 2 -> mix_007.B
    rockygroundshader.links.new(group_input_1.outputs[3], mix_007.inputs[7])
    # group_input_1.Rocks Detail -> mix.Factor
    rockygroundshader.links.new(group_input_1.outputs[4], mix.inputs[0])
    # group_input_1.Large Rocks Scale -> voronoi_texture.Scale
    rockygroundshader.links.new(group_input_1.outputs[5], voronoi_texture.inputs[2])
    # group_input_1.Small Rocks Scale -> voronoi_texture_001.Scale
    rockygroundshader.links.new(group_input_1.outputs[6], voronoi_texture_001.inputs[2])
    # group_input_1.Dirt Color 1 -> mix_005.A
    rockygroundshader.links.new(group_input_1.outputs[7], mix_005.inputs[6])
    # group_input_1.Dirt Color 2 -> mix_005.B
    rockygroundshader.links.new(group_input_1.outputs[8], mix_005.inputs[7])
    # group_input_1.Dirt Color 3 -> mix_006.B
    rockygroundshader.links.new(group_input_1.outputs[9], mix_006.inputs[7])
    # group_input_1.Roughness -> hue_saturation_value.Value
    rockygroundshader.links.new(
        group_input_1.outputs[10], hue_saturation_value.inputs[2]
    )
    # group_input_1.Dirt Bump Strength -> bump.Strength
    rockygroundshader.links.new(group_input_1.outputs[11], bump.inputs[0])
    # group_input_1.Dirt Bump Strength -> bump_002.Strength
    rockygroundshader.links.new(group_input_1.outputs[11], bump_002.inputs[0])
    # group_input_1.Rock Bump Strength -> bump_001.Strength
    rockygroundshader.links.new(group_input_1.outputs[12], bump_001.inputs[0])
    # color_ramp_006.Color -> clamp.Value
    rockygroundshader.links.new(color_ramp_006.outputs[0], clamp.inputs[0])
    # clamp.Result -> noise_texture_006.Roughness
    rockygroundshader.links.new(clamp.outputs[0], noise_texture_006.inputs[4])
    # group_input_1.Extra Bump Strength -> bump_003.Strength
    rockygroundshader.links.new(group_input_1.outputs[13], bump_003.inputs[0])
    # math_1.Value -> bump_003.Height
    rockygroundshader.links.new(math_1.outputs[0], bump_003.inputs[2])
    # bump_003.Normal -> bump.Normal
    rockygroundshader.links.new(bump_003.outputs[0], bump.inputs[3])
    # group_001.0 -> map_range_004.Value
    rockygroundshader.links.new(group_001.outputs[0], map_range_004.inputs[0])
    # map_range_004.Result -> mapping.Location
    rockygroundshader.links.new(map_range_004.outputs[0], mapping.inputs[1])
    return rockygroundshader


rockygroundshader = rockygroundshader_node_group()


# initialize SandShader node group
def sandshader_node_group():
    sandshader = bpy.data.node_groups.new(type="ShaderNodeTree", name="SandShader")

    sandshader.color_tag = "NONE"
    sandshader.description = ""
    sandshader.default_group_node_width = 140

    # sandshader interface
    # Socket BSDF
    bsdf_socket = sandshader.interface.new_socket(
        name="BSDF", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    bsdf_socket.attribute_domain = "POINT"

    # Socket Scale
    scale_socket_1 = sandshader.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    scale_socket_1.default_value = 1.0
    scale_socket_1.min_value = 0.0
    scale_socket_1.max_value = 3.4028234663852886e38
    scale_socket_1.subtype = "NONE"
    scale_socket_1.attribute_domain = "POINT"

    # Socket Rock Scale
    rock_scale_socket = sandshader.interface.new_socket(
        name="Rock Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    rock_scale_socket.default_value = 135.0
    rock_scale_socket.min_value = -1000.0
    rock_scale_socket.max_value = 1000.0
    rock_scale_socket.subtype = "NONE"
    rock_scale_socket.attribute_domain = "POINT"

    # Socket Rock Individual Size
    rock_individual_size_socket = sandshader.interface.new_socket(
        name="Rock Individual Size", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    rock_individual_size_socket.default_value = 1.0
    rock_individual_size_socket.min_value = 0.0
    rock_individual_size_socket.max_value = 2.0
    rock_individual_size_socket.subtype = "NONE"
    rock_individual_size_socket.attribute_domain = "POINT"

    # Socket Rock Color
    rock_color_socket = sandshader.interface.new_socket(
        name="Rock Color", in_out="INPUT", socket_type="NodeSocketColor"
    )
    rock_color_socket.default_value = (0.5, 0.5, 0.5, 1.0)
    rock_color_socket.attribute_domain = "POINT"

    # Socket Sand Color 1
    sand_color_1_socket = sandshader.interface.new_socket(
        name="Sand Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    sand_color_1_socket.default_value = (0.5, 0.5, 0.5, 1.0)
    sand_color_1_socket.attribute_domain = "POINT"

    # Socket Sand Color 2
    sand_color_2_socket = sandshader.interface.new_socket(
        name="Sand Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    sand_color_2_socket.default_value = (0.5, 0.5, 0.5, 1.0)
    sand_color_2_socket.attribute_domain = "POINT"

    # Socket Detail
    detail_socket = sandshader.interface.new_socket(
        name="Detail", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    detail_socket.default_value = 15.0
    detail_socket.min_value = 0.0
    detail_socket.max_value = 15.0
    detail_socket.subtype = "NONE"
    detail_socket.attribute_domain = "POINT"

    # Socket Roughness
    roughness_socket_1 = sandshader.interface.new_socket(
        name="Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    roughness_socket_1.default_value = 0.5
    roughness_socket_1.min_value = 0.0
    roughness_socket_1.max_value = 1.0
    roughness_socket_1.subtype = "FACTOR"
    roughness_socket_1.attribute_domain = "POINT"

    # Socket Sand Bump Strength 1
    sand_bump_strength_1_socket = sandshader.interface.new_socket(
        name="Sand Bump Strength 1", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    sand_bump_strength_1_socket.default_value = 0.10000000149011612
    sand_bump_strength_1_socket.min_value = 0.0
    sand_bump_strength_1_socket.max_value = 1.0
    sand_bump_strength_1_socket.subtype = "FACTOR"
    sand_bump_strength_1_socket.attribute_domain = "POINT"

    # Socket Sand Bump Strength 2
    sand_bump_strength_2_socket = sandshader.interface.new_socket(
        name="Sand Bump Strength 2", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    sand_bump_strength_2_socket.default_value = 0.10000000149011612
    sand_bump_strength_2_socket.min_value = 0.0
    sand_bump_strength_2_socket.max_value = 1.0
    sand_bump_strength_2_socket.subtype = "FACTOR"
    sand_bump_strength_2_socket.attribute_domain = "POINT"

    # Socket Rock Bump Strength
    rock_bump_strength_socket_1 = sandshader.interface.new_socket(
        name="Rock Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    rock_bump_strength_socket_1.default_value = 0.30000001192092896
    rock_bump_strength_socket_1.min_value = 0.0
    rock_bump_strength_socket_1.max_value = 1.0
    rock_bump_strength_socket_1.subtype = "FACTOR"
    rock_bump_strength_socket_1.attribute_domain = "POINT"

    # initialize sandshader nodes
    # node Group Output
    group_output_2 = sandshader.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True

    # node Group Input
    group_input_2 = sandshader.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"

    # node Principled BSDF
    principled_bsdf_1 = sandshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_1.name = "Principled BSDF"
    principled_bsdf_1.distribution = "MULTI_GGX"
    principled_bsdf_1.subsurface_method = "RANDOM_WALK"
    # Metallic
    principled_bsdf_1.inputs[1].default_value = 0.0
    # IOR
    principled_bsdf_1.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf_1.inputs[4].default_value = 1.0
    # Diffuse Roughness
    principled_bsdf_1.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf_1.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf_1.inputs[9].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf_1.inputs[10].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf_1.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf_1.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf_1.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf_1.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf_1.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf_1.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf_1.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf_1.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf_1.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf_1.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf_1.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf_1.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf_1.inputs[24].default_value = 0.0
    # Sheen Roughness
    principled_bsdf_1.inputs[25].default_value = 0.5
    # Sheen Tint
    principled_bsdf_1.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf_1.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf_1.inputs[28].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf_1.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf_1.inputs[30].default_value = 1.3300000429153442

    # node Mapping
    mapping_1 = sandshader.nodes.new("ShaderNodeMapping")
    mapping_1.name = "Mapping"
    mapping_1.vector_type = "POINT"
    # Rotation
    mapping_1.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Texture Coordinate
    texture_coordinate_1 = sandshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_1.name = "Texture Coordinate"
    texture_coordinate_1.from_instancer = False
    texture_coordinate_1.outputs[0].hide = True
    texture_coordinate_1.outputs[1].hide = True
    texture_coordinate_1.outputs[2].hide = True
    texture_coordinate_1.outputs[4].hide = True
    texture_coordinate_1.outputs[5].hide = True
    texture_coordinate_1.outputs[6].hide = True

    # node Voronoi Texture
    voronoi_texture_1 = sandshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_1.name = "Voronoi Texture"
    voronoi_texture_1.distance = "EUCLIDEAN"
    voronoi_texture_1.feature = "F1"
    voronoi_texture_1.normalize = False
    voronoi_texture_1.voronoi_dimensions = "3D"
    # Detail
    voronoi_texture_1.inputs[3].default_value = 2.0
    # Roughness
    voronoi_texture_1.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture_1.inputs[5].default_value = 1.7000000476837158
    # Randomness
    voronoi_texture_1.inputs[8].default_value = 1.0

    # node Hue/Saturation/Value
    hue_saturation_value_1 = sandshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_1.name = "Hue/Saturation/Value"
    # Hue
    hue_saturation_value_1.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value_1.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value_1.inputs[3].default_value = 1.0

    # node Color Ramp.001
    color_ramp_001_1 = sandshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001_1.name = "Color Ramp.001"
    color_ramp_001_1.color_ramp.color_mode = "RGB"
    color_ramp_001_1.color_ramp.hue_interpolation = "NEAR"
    color_ramp_001_1.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_001_1.color_ramp.elements.remove(color_ramp_001_1.color_ramp.elements[0])
    color_ramp_001_1_cre_0 = color_ramp_001_1.color_ramp.elements[0]
    color_ramp_001_1_cre_0.position = 0.6227270364761353
    color_ramp_001_1_cre_0.alpha = 1.0
    color_ramp_001_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_001_1_cre_1 = color_ramp_001_1.color_ramp.elements.new(
        0.6272730827331543
    )
    color_ramp_001_1_cre_1.alpha = 1.0
    color_ramp_001_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Color Ramp.002
    color_ramp_002_1 = sandshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_002_1.name = "Color Ramp.002"
    color_ramp_002_1.color_ramp.color_mode = "RGB"
    color_ramp_002_1.color_ramp.hue_interpolation = "NEAR"
    color_ramp_002_1.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_002_1.color_ramp.elements.remove(color_ramp_002_1.color_ramp.elements[0])
    color_ramp_002_1_cre_0 = color_ramp_002_1.color_ramp.elements[0]
    color_ramp_002_1_cre_0.position = 0.0
    color_ramp_002_1_cre_0.alpha = 1.0
    color_ramp_002_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_002_1_cre_1 = color_ramp_002_1.color_ramp.elements.new(
        0.6272730827331543
    )
    color_ramp_002_1_cre_1.alpha = 1.0
    color_ramp_002_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Noise Texture
    noise_texture_1 = sandshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_1.name = "Noise Texture"
    noise_texture_1.noise_dimensions = "3D"
    noise_texture_1.noise_type = "FBM"
    noise_texture_1.normalize = True
    # Scale
    noise_texture_1.inputs[2].default_value = 15.0
    # Roughness
    noise_texture_1.inputs[4].default_value = 0.4000000059604645
    # Lacunarity
    noise_texture_1.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_1.inputs[8].default_value = 0.0

    # node Mix.001
    mix_001_1 = sandshader.nodes.new("ShaderNodeMix")
    mix_001_1.name = "Mix.001"
    mix_001_1.blend_type = "MIX"
    mix_001_1.clamp_factor = True
    mix_001_1.clamp_result = False
    mix_001_1.data_type = "RGBA"
    mix_001_1.factor_mode = "UNIFORM"

    # node Mix.003
    mix_003_1 = sandshader.nodes.new("ShaderNodeMix")
    mix_003_1.name = "Mix.003"
    mix_003_1.blend_type = "MIX"
    mix_003_1.clamp_factor = True
    mix_003_1.clamp_result = False
    mix_003_1.data_type = "RGBA"
    mix_003_1.factor_mode = "UNIFORM"

    # node Noise Texture.001
    noise_texture_001_1 = sandshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001_1.name = "Noise Texture.001"
    noise_texture_001_1.noise_dimensions = "3D"
    noise_texture_001_1.noise_type = "FBM"
    noise_texture_001_1.normalize = True
    # Scale
    noise_texture_001_1.inputs[2].default_value = 15.0
    # Roughness
    noise_texture_001_1.inputs[4].default_value = 0.699999988079071
    # Lacunarity
    noise_texture_001_1.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001_1.inputs[8].default_value = 0.0

    # node Bump
    bump_1 = sandshader.nodes.new("ShaderNodeBump")
    bump_1.name = "Bump"
    bump_1.invert = False
    # Distance
    bump_1.inputs[1].default_value = 1.0
    # Normal
    bump_1.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Bump.001
    bump_001_1 = sandshader.nodes.new("ShaderNodeBump")
    bump_001_1.name = "Bump.001"
    bump_001_1.invert = False
    # Distance
    bump_001_1.inputs[1].default_value = 1.0

    # node Bump.002
    bump_002_1 = sandshader.nodes.new("ShaderNodeBump")
    bump_002_1.name = "Bump.002"
    bump_002_1.invert = False
    # Distance
    bump_002_1.inputs[1].default_value = 1.0

    # node Group.001
    group_001_1 = sandshader.nodes.new("ShaderNodeGroup")
    group_001_1.name = "Group.001"
    group_001_1.node_tree = random_x4___mat
    # Socket_5
    group_001_1.inputs[0].default_value = 0.23152099549770355

    # node Map Range.004
    map_range_004_1 = sandshader.nodes.new("ShaderNodeMapRange")
    map_range_004_1.name = "Map Range.004"
    map_range_004_1.clamp = True
    map_range_004_1.data_type = "FLOAT"
    map_range_004_1.interpolation_type = "LINEAR"
    # From Min
    map_range_004_1.inputs[1].default_value = 0.0
    # From Max
    map_range_004_1.inputs[2].default_value = 1.0
    # To Min
    map_range_004_1.inputs[3].default_value = -1000.0
    # To Max
    map_range_004_1.inputs[4].default_value = 1000.0

    # Set locations
    group_output_2.location = (1379.55322265625, 0.0)
    group_input_2.location = (-1384.84765625, -4.3114013671875)
    principled_bsdf_1.location = (1089.55322265625, 118.02996826171875)
    mapping_1.location = (-866.49755859375, 132.17681884765625)
    texture_coordinate_1.location = (-1089.55322265625, 130.88543701171875)
    voronoi_texture_1.location = (-461.566162109375, 374.72833251953125)
    hue_saturation_value_1.location = (-261.241455078125, 293.3447570800781)
    color_ramp_001_1.location = (-31.5291748046875, 490.95660400390625)
    color_ramp_002_1.location = (-23.26904296875, 194.15069580078125)
    noise_texture_1.location = (-438.474365234375, -71.4677734375)
    mix_001_1.location = (63.28466796875, -101.11846923828125)
    mix_003_1.location = (446.49908447265625, 243.61837768554688)
    noise_texture_001_1.location = (-447.4490966796875, -490.95660400390625)
    bump_1.location = (-198.7718505859375, -482.04693603515625)
    bump_001_1.location = (2.1358642578125, -481.17681884765625)
    bump_002_1.location = (188.2581787109375, -488.13763427734375)
    group_001_1.location = (-1507.3045654296875, 424.6938171386719)
    map_range_004_1.location = (-1326.2952880859375, 294.6138000488281)

    # initialize sandshader links
    # color_ramp_001_1.Color -> mix_003_1.Factor
    sandshader.links.new(color_ramp_001_1.outputs[0], mix_003_1.inputs[0])
    # bump_1.Normal -> bump_001_1.Normal
    sandshader.links.new(bump_1.outputs[0], bump_001_1.inputs[3])
    # noise_texture_1.Fac -> bump_1.Height
    sandshader.links.new(noise_texture_1.outputs[0], bump_1.inputs[2])
    # texture_coordinate_1.Object -> mapping_1.Vector
    sandshader.links.new(texture_coordinate_1.outputs[3], mapping_1.inputs[0])
    # mapping_1.Vector -> voronoi_texture_1.Vector
    sandshader.links.new(mapping_1.outputs[0], voronoi_texture_1.inputs[0])
    # noise_texture_001_1.Fac -> bump_001_1.Height
    sandshader.links.new(noise_texture_001_1.outputs[0], bump_001_1.inputs[2])
    # mix_001_1.Result -> mix_003_1.B
    sandshader.links.new(mix_001_1.outputs[2], mix_003_1.inputs[7])
    # mapping_1.Vector -> noise_texture_001_1.Vector
    sandshader.links.new(mapping_1.outputs[0], noise_texture_001_1.inputs[0])
    # bump_002_1.Normal -> principled_bsdf_1.Normal
    sandshader.links.new(bump_002_1.outputs[0], principled_bsdf_1.inputs[5])
    # color_ramp_002_1.Color -> bump_002_1.Height
    sandshader.links.new(color_ramp_002_1.outputs[0], bump_002_1.inputs[2])
    # bump_001_1.Normal -> bump_002_1.Normal
    sandshader.links.new(bump_001_1.outputs[0], bump_002_1.inputs[3])
    # hue_saturation_value_1.Color -> color_ramp_001_1.Fac
    sandshader.links.new(hue_saturation_value_1.outputs[0], color_ramp_001_1.inputs[0])
    # voronoi_texture_1.Color -> hue_saturation_value_1.Color
    sandshader.links.new(voronoi_texture_1.outputs[1], hue_saturation_value_1.inputs[4])
    # hue_saturation_value_1.Color -> color_ramp_002_1.Fac
    sandshader.links.new(hue_saturation_value_1.outputs[0], color_ramp_002_1.inputs[0])
    # mapping_1.Vector -> noise_texture_1.Vector
    sandshader.links.new(mapping_1.outputs[0], noise_texture_1.inputs[0])
    # mix_003_1.Result -> principled_bsdf_1.Base Color
    sandshader.links.new(mix_003_1.outputs[2], principled_bsdf_1.inputs[0])
    # noise_texture_1.Fac -> mix_001_1.Factor
    sandshader.links.new(noise_texture_1.outputs[0], mix_001_1.inputs[0])
    # principled_bsdf_1.BSDF -> group_output_2.BSDF
    sandshader.links.new(principled_bsdf_1.outputs[0], group_output_2.inputs[0])
    # group_input_2.Scale -> mapping_1.Scale
    sandshader.links.new(group_input_2.outputs[0], mapping_1.inputs[3])
    # group_input_2.Rock Scale -> voronoi_texture_1.Scale
    sandshader.links.new(group_input_2.outputs[1], voronoi_texture_1.inputs[2])
    # group_input_2.Rock Individual Size -> hue_saturation_value_1.Value
    sandshader.links.new(group_input_2.outputs[2], hue_saturation_value_1.inputs[2])
    # group_input_2.Rock Color -> mix_003_1.A
    sandshader.links.new(group_input_2.outputs[3], mix_003_1.inputs[6])
    # group_input_2.Sand Color 1 -> mix_001_1.A
    sandshader.links.new(group_input_2.outputs[4], mix_001_1.inputs[6])
    # group_input_2.Sand Color 2 -> mix_001_1.B
    sandshader.links.new(group_input_2.outputs[5], mix_001_1.inputs[7])
    # group_input_2.Detail -> noise_texture_1.Detail
    sandshader.links.new(group_input_2.outputs[6], noise_texture_1.inputs[3])
    # group_input_2.Detail -> noise_texture_001_1.Detail
    sandshader.links.new(group_input_2.outputs[6], noise_texture_001_1.inputs[3])
    # group_input_2.Roughness -> principled_bsdf_1.Roughness
    sandshader.links.new(group_input_2.outputs[7], principled_bsdf_1.inputs[2])
    # group_input_2.Sand Bump Strength 1 -> bump_1.Strength
    sandshader.links.new(group_input_2.outputs[8], bump_1.inputs[0])
    # group_input_2.Sand Bump Strength 2 -> bump_001_1.Strength
    sandshader.links.new(group_input_2.outputs[9], bump_001_1.inputs[0])
    # group_input_2.Rock Bump Strength -> bump_002_1.Strength
    sandshader.links.new(group_input_2.outputs[10], bump_002_1.inputs[0])
    # group_001_1.0 -> map_range_004_1.Value
    sandshader.links.new(group_001_1.outputs[0], map_range_004_1.inputs[0])
    # map_range_004_1.Result -> mapping_1.Location
    sandshader.links.new(map_range_004_1.outputs[0], mapping_1.inputs[1])
    return sandshader


sandshader = sandshader_node_group()


# initialize Random x2 | Mat node group
def random_x2___mat_node_group():
    random_x2___mat = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="Random x2 | Mat"
    )

    random_x2___mat.color_tag = "NONE"
    random_x2___mat.description = ""
    random_x2___mat.default_group_node_width = 140

    # random_x2___mat interface
    # Socket 0
    _0_socket_1 = random_x2___mat.interface.new_socket(
        name="0", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    _0_socket_1.default_value = 0.0
    _0_socket_1.min_value = 0.0
    _0_socket_1.max_value = 1.0
    _0_socket_1.subtype = "NONE"
    _0_socket_1.attribute_domain = "POINT"

    # Socket 1
    _1_socket_1 = random_x2___mat.interface.new_socket(
        name="1", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    _1_socket_1.default_value = 0.0
    _1_socket_1.min_value = 0.0
    _1_socket_1.max_value = 1.0
    _1_socket_1.subtype = "NONE"
    _1_socket_1.attribute_domain = "POINT"

    # Socket 2
    _2_socket_1 = random_x2___mat.interface.new_socket(
        name="2", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    _2_socket_1.default_value = 0.0
    _2_socket_1.min_value = -3.4028234663852886e38
    _2_socket_1.max_value = 3.4028234663852886e38
    _2_socket_1.subtype = "NONE"
    _2_socket_1.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_1 = random_x2___mat.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    seed_socket_1.default_value = 0.0
    seed_socket_1.min_value = 0.0
    seed_socket_1.max_value = 1.0
    seed_socket_1.subtype = "NONE"
    seed_socket_1.attribute_domain = "POINT"

    # initialize random_x2___mat nodes
    # node Group Output
    group_output_3 = random_x2___mat.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True

    # node Group Input
    group_input_3 = random_x2___mat.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"

    # node Object Info
    object_info_1 = random_x2___mat.nodes.new("ShaderNodeObjectInfo")
    object_info_1.name = "Object Info"

    # node Math
    math_2 = random_x2___mat.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = "ADD"
    math_2.use_clamp = False

    # node White Noise Texture
    white_noise_texture_1 = random_x2___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_1.name = "White Noise Texture"
    white_noise_texture_1.noise_dimensions = "4D"

    # node Separate Color
    separate_color_1 = random_x2___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color_1.name = "Separate Color"
    separate_color_1.mode = "RGB"

    # Set locations
    group_output_3.location = (689.6586303710938, -17.691898345947266)
    group_input_3.location = (-490.65618896484375, 343.00933837890625)
    object_info_1.location = (-490.65618896484375, 63.65891647338867)
    math_2.location = (-280.6562194824219, 343.00933837890625)
    white_noise_texture_1.location = (-70.65621948242188, 343.00933837890625)
    separate_color_1.location = (139.34378051757812, 343.00933837890625)

    # initialize random_x2___mat links
    # object_info_1.Random -> white_noise_texture_1.W
    random_x2___mat.links.new(object_info_1.outputs[5], white_noise_texture_1.inputs[1])
    # math_2.Value -> white_noise_texture_1.Vector
    random_x2___mat.links.new(math_2.outputs[0], white_noise_texture_1.inputs[0])
    # white_noise_texture_1.Color -> separate_color_1.Color
    random_x2___mat.links.new(
        white_noise_texture_1.outputs[1], separate_color_1.inputs[0]
    )
    # object_info_1.Object Index -> math_2.Value
    random_x2___mat.links.new(object_info_1.outputs[3], math_2.inputs[1])
    # group_input_3.Seed -> math_2.Value
    random_x2___mat.links.new(group_input_3.outputs[0], math_2.inputs[0])
    # separate_color_1.Red -> group_output_3.0
    random_x2___mat.links.new(separate_color_1.outputs[0], group_output_3.inputs[0])
    # separate_color_1.Green -> group_output_3.1
    random_x2___mat.links.new(separate_color_1.outputs[1], group_output_3.inputs[1])
    # separate_color_1.Blue -> group_output_3.2
    random_x2___mat.links.new(separate_color_1.outputs[2], group_output_3.inputs[2])
    return random_x2___mat


random_x2___mat = random_x2___mat_node_group()


# initialize RockShader | 3 node group
def rockshader___3_node_group():
    rockshader___3 = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="RockShader | 3"
    )

    rockshader___3.color_tag = "NONE"
    rockshader___3.description = ""
    rockshader___3.default_group_node_width = 140

    # rockshader___3 interface
    # Socket Shader
    shader_socket_1 = rockshader___3.interface.new_socket(
        name="Shader", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    shader_socket_1.attribute_domain = "POINT"

    # Socket Scale
    scale_socket_2 = rockshader___3.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    scale_socket_2.default_value = 1.0
    scale_socket_2.min_value = -3.4028234663852886e38
    scale_socket_2.max_value = 3.4028234663852886e38
    scale_socket_2.subtype = "NONE"
    scale_socket_2.attribute_domain = "POINT"

    # Socket Color 1
    color_1_socket = rockshader___3.interface.new_socket(
        name="Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_1_socket.default_value = (1.0, 0.33455199003219604, 0.12201099842786789, 1.0)
    color_1_socket.attribute_domain = "POINT"

    # Socket Color 2
    color_2_socket = rockshader___3.interface.new_socket(
        name="Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_2_socket.default_value = (
        0.10239599645137787,
        0.009690999984741211,
        0.0059830001555383205,
        1.0,
    )
    color_2_socket.attribute_domain = "POINT"

    # Socket Color 3
    color_3_socket = rockshader___3.interface.new_socket(
        name="Color 3", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_3_socket.default_value = (
        0.13511300086975098,
        0.041269998997449875,
        0.015100999735295773,
        1.0,
    )
    color_3_socket.attribute_domain = "POINT"

    # Socket Color 4
    color_4_socket = rockshader___3.interface.new_socket(
        name="Color 4", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_4_socket.default_value = (1.0, 0.27467700839042664, 0.0886560007929802, 1.0)
    color_4_socket.attribute_domain = "POINT"

    # Socket Noise Scale
    noise_scale_socket = rockshader___3.interface.new_socket(
        name="Noise Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_scale_socket.default_value = 16.0
    noise_scale_socket.min_value = -1000.0
    noise_scale_socket.max_value = 1000.0
    noise_scale_socket.subtype = "NONE"
    noise_scale_socket.attribute_domain = "POINT"

    # Socket Chunks Scale
    chunks_scale_socket = rockshader___3.interface.new_socket(
        name="Chunks Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    chunks_scale_socket.default_value = 4.0
    chunks_scale_socket.min_value = -1000.0
    chunks_scale_socket.max_value = 1000.0
    chunks_scale_socket.subtype = "NONE"
    chunks_scale_socket.attribute_domain = "POINT"

    # Socket Noise Detail 1
    noise_detail_1_socket = rockshader___3.interface.new_socket(
        name="Noise Detail 1", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_detail_1_socket.default_value = 15.0
    noise_detail_1_socket.min_value = 0.0
    noise_detail_1_socket.max_value = 15.0
    noise_detail_1_socket.subtype = "NONE"
    noise_detail_1_socket.attribute_domain = "POINT"

    # Socket Noise Detail 2
    noise_detail_2_socket = rockshader___3.interface.new_socket(
        name="Noise Detail 2", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_detail_2_socket.default_value = 0.44999998807907104
    noise_detail_2_socket.min_value = 0.0
    noise_detail_2_socket.max_value = 1.0
    noise_detail_2_socket.subtype = "FACTOR"
    noise_detail_2_socket.attribute_domain = "POINT"

    # Socket Distortion
    distortion_socket = rockshader___3.interface.new_socket(
        name="Distortion", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    distortion_socket.default_value = 0.10000000149011612
    distortion_socket.min_value = 0.0
    distortion_socket.max_value = 1.0
    distortion_socket.subtype = "FACTOR"
    distortion_socket.attribute_domain = "POINT"

    # Socket Roughness
    roughness_socket_2 = rockshader___3.interface.new_socket(
        name="Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    roughness_socket_2.default_value = 1.0
    roughness_socket_2.min_value = 0.0
    roughness_socket_2.max_value = 2.0
    roughness_socket_2.subtype = "NONE"
    roughness_socket_2.attribute_domain = "POINT"

    # Socket Noise Bump Strength
    noise_bump_strength_socket = rockshader___3.interface.new_socket(
        name="Noise Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_bump_strength_socket.default_value = 0.20000000298023224
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = "FACTOR"
    noise_bump_strength_socket.attribute_domain = "POINT"

    # Socket Detail Bump Strength
    detail_bump_strength_socket = rockshader___3.interface.new_socket(
        name="Detail Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    detail_bump_strength_socket.default_value = 0.10000000149011612
    detail_bump_strength_socket.min_value = 0.0
    detail_bump_strength_socket.max_value = 1.0
    detail_bump_strength_socket.subtype = "FACTOR"
    detail_bump_strength_socket.attribute_domain = "POINT"

    # initialize rockshader___3 nodes
    # node Group Output
    group_output_4 = rockshader___3.nodes.new("NodeGroupOutput")
    group_output_4.name = "Group Output"
    group_output_4.is_active_output = True

    # node Texture Coordinate
    texture_coordinate_2 = rockshader___3.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_2.name = "Texture Coordinate"
    texture_coordinate_2.from_instancer = False

    # node Mapping.001
    mapping_001 = rockshader___3.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = "POINT"
    # Location
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    mapping_001.inputs[3].default_value = (1.0, 1.0, 1.5)

    # node Noise Texture.001
    noise_texture_001_2 = rockshader___3.nodes.new("ShaderNodeTexNoise")
    noise_texture_001_2.name = "Noise Texture.001"
    noise_texture_001_2.noise_dimensions = "3D"
    noise_texture_001_2.noise_type = "FBM"
    noise_texture_001_2.normalize = True
    # Scale
    noise_texture_001_2.inputs[2].default_value = 19.0
    # Detail
    noise_texture_001_2.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_001_2.inputs[4].default_value = 0.699999988079071
    # Lacunarity
    noise_texture_001_2.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001_2.inputs[8].default_value = 0.0

    # node ColorRamp.001
    colorramp_001 = rockshader___3.nodes.new("ShaderNodeValToRGB")
    colorramp_001.name = "ColorRamp.001"
    colorramp_001.color_ramp.color_mode = "RGB"
    colorramp_001.color_ramp.hue_interpolation = "NEAR"
    colorramp_001.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_001.color_ramp.elements.remove(colorramp_001.color_ramp.elements[0])
    colorramp_001_cre_0 = colorramp_001.color_ramp.elements[0]
    colorramp_001_cre_0.position = 0.0
    colorramp_001_cre_0.alpha = 1.0
    colorramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_001_cre_1 = colorramp_001.color_ramp.elements.new(0.604113757610321)
    colorramp_001_cre_1.alpha = 1.0
    colorramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Mix.001
    mix_001_2 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_001_2.name = "Mix.001"
    mix_001_2.blend_type = "MIX"
    mix_001_2.clamp_factor = True
    mix_001_2.clamp_result = False
    mix_001_2.data_type = "RGBA"
    mix_001_2.factor_mode = "UNIFORM"
    # A_Color
    mix_001_2.inputs[6].default_value = (
        0.14487500488758087,
        0.14487500488758087,
        0.14487500488758087,
        1.0,
    )

    # node ColorRamp.003
    colorramp_003 = rockshader___3.nodes.new("ShaderNodeValToRGB")
    colorramp_003.name = "ColorRamp.003"
    colorramp_003.color_ramp.color_mode = "RGB"
    colorramp_003.color_ramp.hue_interpolation = "NEAR"
    colorramp_003.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_003.color_ramp.elements.remove(colorramp_003.color_ramp.elements[0])
    colorramp_003_cre_0 = colorramp_003.color_ramp.elements[0]
    colorramp_003_cre_0.position = 0.0
    colorramp_003_cre_0.alpha = 1.0
    colorramp_003_cre_0.color = (
        0.5663849711418152,
        0.5663849711418152,
        0.5663849711418152,
        1.0,
    )

    colorramp_003_cre_1 = colorramp_003.color_ramp.elements.new(1.0)
    colorramp_003_cre_1.alpha = 1.0
    colorramp_003_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Voronoi Texture
    voronoi_texture_2 = rockshader___3.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_2.name = "Voronoi Texture"
    voronoi_texture_2.distance = "EUCLIDEAN"
    voronoi_texture_2.feature = "F1"
    voronoi_texture_2.normalize = False
    voronoi_texture_2.voronoi_dimensions = "3D"
    # Scale
    voronoi_texture_2.inputs[2].default_value = 350.0
    # Detail
    voronoi_texture_2.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_2.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture_2.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture_2.inputs[8].default_value = 1.0

    # node Bump.001
    bump_001_2 = rockshader___3.nodes.new("ShaderNodeBump")
    bump_001_2.name = "Bump.001"
    bump_001_2.invert = False
    # Distance
    bump_001_2.inputs[1].default_value = 1.0

    # node Principled BSDF
    principled_bsdf_2 = rockshader___3.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_2.name = "Principled BSDF"
    principled_bsdf_2.distribution = "GGX"
    principled_bsdf_2.subsurface_method = "RANDOM_WALK_SKIN"
    # Metallic
    principled_bsdf_2.inputs[1].default_value = 0.0
    # IOR
    principled_bsdf_2.inputs[3].default_value = 1.4500000476837158
    # Alpha
    principled_bsdf_2.inputs[4].default_value = 1.0
    # Diffuse Roughness
    principled_bsdf_2.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf_2.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf_2.inputs[9].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf_2.inputs[10].default_value = 0.05000000074505806
    # Subsurface IOR
    principled_bsdf_2.inputs[11].default_value = 1.399999976158142
    # Subsurface Anisotropy
    principled_bsdf_2.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf_2.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf_2.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf_2.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf_2.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf_2.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf_2.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf_2.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf_2.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf_2.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf_2.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf_2.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf_2.inputs[24].default_value = 0.0
    # Sheen Roughness
    principled_bsdf_2.inputs[25].default_value = 0.5
    # Sheen Tint
    principled_bsdf_2.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf_2.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
    # Emission Strength
    principled_bsdf_2.inputs[28].default_value = 1.0
    # Thin Film Thickness
    principled_bsdf_2.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf_2.inputs[30].default_value = 1.3300000429153442

    # node Mapping
    mapping_2 = rockshader___3.nodes.new("ShaderNodeMapping")
    mapping_2.name = "Mapping"
    mapping_2.vector_type = "POINT"
    # Rotation
    mapping_2.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node ColorRamp.002
    colorramp_002 = rockshader___3.nodes.new("ShaderNodeValToRGB")
    colorramp_002.name = "ColorRamp.002"
    colorramp_002.color_ramp.color_mode = "RGB"
    colorramp_002.color_ramp.hue_interpolation = "NEAR"
    colorramp_002.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_002.color_ramp.elements.remove(colorramp_002.color_ramp.elements[0])
    colorramp_002_cre_0 = colorramp_002.color_ramp.elements[0]
    colorramp_002_cre_0.position = 0.08226212114095688
    colorramp_002_cre_0.alpha = 1.0
    colorramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_002_cre_1 = colorramp_002.color_ramp.elements.new(0.15424175560474396)
    colorramp_002_cre_1.alpha = 1.0
    colorramp_002_cre_1.color = (
        0.3593989908695221,
        0.3593989908695221,
        0.3593989908695221,
        1.0,
    )

    colorramp_002_cre_2 = colorramp_002.color_ramp.elements.new(0.2776348292827606)
    colorramp_002_cre_2.alpha = 1.0
    colorramp_002_cre_2.color = (0.0, 0.0, 0.0, 1.0)

    # node ColorRamp
    colorramp = rockshader___3.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = "RGB"
    colorramp.color_ramp.hue_interpolation = "NEAR"
    colorramp.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.010282879695296288
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (1.0, 1.0, 1.0, 1.0)

    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.15167097747325897)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.0, 0.0, 0.0, 1.0)

    # node Mix.002
    mix_002_1 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_002_1.name = "Mix.002"
    mix_002_1.blend_type = "MIX"
    mix_002_1.clamp_factor = True
    mix_002_1.clamp_result = False
    mix_002_1.data_type = "RGBA"
    mix_002_1.factor_mode = "UNIFORM"

    # node Mix.003
    mix_003_2 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_003_2.name = "Mix.003"
    mix_003_2.blend_type = "MIX"
    mix_003_2.clamp_factor = True
    mix_003_2.clamp_result = False
    mix_003_2.data_type = "RGBA"
    mix_003_2.factor_mode = "UNIFORM"

    # node Mix.004
    mix_004_1 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_004_1.name = "Mix.004"
    mix_004_1.blend_type = "LIGHTEN"
    mix_004_1.clamp_factor = True
    mix_004_1.clamp_result = False
    mix_004_1.data_type = "RGBA"
    mix_004_1.factor_mode = "UNIFORM"

    # node Voronoi Texture.001
    voronoi_texture_001_1 = rockshader___3.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001_1.name = "Voronoi Texture.001"
    voronoi_texture_001_1.distance = "EUCLIDEAN"
    voronoi_texture_001_1.feature = "DISTANCE_TO_EDGE"
    voronoi_texture_001_1.normalize = False
    voronoi_texture_001_1.voronoi_dimensions = "3D"
    # Detail
    voronoi_texture_001_1.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_001_1.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture_001_1.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture_001_1.inputs[8].default_value = 1.0

    # node Noise Texture
    noise_texture_2 = rockshader___3.nodes.new("ShaderNodeTexNoise")
    noise_texture_2.name = "Noise Texture"
    noise_texture_2.noise_dimensions = "3D"
    noise_texture_2.noise_type = "FBM"
    noise_texture_2.normalize = True
    # Lacunarity
    noise_texture_2.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_2.inputs[8].default_value = 0.0

    # node Mix
    mix_1 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_1.name = "Mix"
    mix_1.blend_type = "LINEAR_LIGHT"
    mix_1.clamp_factor = True
    mix_1.clamp_result = False
    mix_1.data_type = "RGBA"
    mix_1.factor_mode = "UNIFORM"

    # node Hue Saturation Value
    hue_saturation_value_2 = rockshader___3.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_2.name = "Hue Saturation Value"
    # Hue
    hue_saturation_value_2.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value_2.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value_2.inputs[3].default_value = 1.0

    # node Bump
    bump_2 = rockshader___3.nodes.new("ShaderNodeBump")
    bump_2.name = "Bump"
    bump_2.invert = False
    # Distance
    bump_2.inputs[1].default_value = 1.0
    # Normal
    bump_2.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Group Input
    group_input_4 = rockshader___3.nodes.new("NodeGroupInput")
    group_input_4.name = "Group Input"

    # node Clamp
    clamp_1 = rockshader___3.nodes.new("ShaderNodeClamp")
    clamp_1.name = "Clamp"
    clamp_1.hide = True
    clamp_1.clamp_type = "MINMAX"
    # Min
    clamp_1.inputs[1].default_value = 0.0
    # Max
    clamp_1.inputs[2].default_value = 1.0

    # node Map Range.011
    map_range_011 = rockshader___3.nodes.new("ShaderNodeMapRange")
    map_range_011.name = "Map Range.011"
    map_range_011.clamp = True
    map_range_011.data_type = "FLOAT"
    map_range_011.interpolation_type = "LINEAR"
    # From Min
    map_range_011.inputs[1].default_value = 0.0
    # From Max
    map_range_011.inputs[2].default_value = 1.0
    # To Min
    map_range_011.inputs[3].default_value = -1000.0
    # To Max
    map_range_011.inputs[4].default_value = 1000.0

    # node Group.001
    group_001_2 = rockshader___3.nodes.new("ShaderNodeGroup")
    group_001_2.name = "Group.001"
    group_001_2.node_tree = random_x2___mat
    # Socket_3
    group_001_2.inputs[0].default_value = 0.5241000056266785

    # Set locations
    group_output_4.location = (1321.0780029296875, 0.0)
    texture_coordinate_2.location = (-1131.0780029296875, -12.876541137695312)
    mapping_001.location = (-770.3403930664062, -10.9368896484375)
    noise_texture_001_2.location = (-503.7137451171875, 421.400390625)
    colorramp_001.location = (-283.625, 445.20013427734375)
    mix_001_2.location = (-19.82373046875, 127.36956787109375)
    colorramp_003.location = (471.98138427734375, -5.3743896484375)
    voronoi_texture_2.location = (-214.30291748046875, 173.81625366210938)
    bump_001_2.location = (813.8541259765625, -215.06895446777344)
    principled_bsdf_2.location = (1028.9171142578125, 249.29254150390625)
    mapping_2.location = (-939.576171875, -12.199813842773438)
    colorramp_002.location = (353.46002197265625, 471.2227783203125)
    colorramp.location = (172.41802978515625, 188.79144287109375)
    mix_002_1.location = (436.03082275390625, 237.861083984375)
    mix_003_2.location = (599.032958984375, 246.4215087890625)
    mix_004_1.location = (766.0985107421875, 244.40390014648438)
    voronoi_texture_001_1.location = (-207.63560485839844, -74.17858123779297)
    noise_texture_2.location = (-564.4707641601562, 2.5886731147766113)
    mix_1.location = (-408.1333923339844, 3.6961328983306885)
    hue_saturation_value_2.location = (787.67919921875, -13.640274047851562)
    bump_2.location = (588.8912353515625, -232.5960235595703)
    group_input_4.location = (-1126.564453125, -255.41787719726562)
    clamp_1.location = (-564.4707641601562, -297.41131591796875)
    map_range_011.location = (-1311.203125, -52.487457275390625)
    group_001_2.location = (-1493.3907470703125, -203.5081329345703)

    # initialize rockshader___3 links
    # colorramp_001.Color -> mix_003_2.Factor
    rockshader___3.links.new(colorramp_001.outputs[0], mix_003_2.inputs[0])
    # mix_003_2.Result -> mix_004_1.A
    rockshader___3.links.new(mix_003_2.outputs[2], mix_004_1.inputs[6])
    # voronoi_texture_2.Distance -> bump_001_2.Height
    rockshader___3.links.new(voronoi_texture_2.outputs[0], bump_001_2.inputs[2])
    # mix_1.Result -> voronoi_texture_2.Vector
    rockshader___3.links.new(mix_1.outputs[2], voronoi_texture_2.inputs[0])
    # bump_001_2.Normal -> principled_bsdf_2.Normal
    rockshader___3.links.new(bump_001_2.outputs[0], principled_bsdf_2.inputs[5])
    # texture_coordinate_2.Object -> mapping_2.Vector
    rockshader___3.links.new(texture_coordinate_2.outputs[3], mapping_2.inputs[0])
    # hue_saturation_value_2.Color -> principled_bsdf_2.Roughness
    rockshader___3.links.new(
        hue_saturation_value_2.outputs[0], principled_bsdf_2.inputs[2]
    )
    # mix_004_1.Result -> principled_bsdf_2.Base Color
    rockshader___3.links.new(mix_004_1.outputs[2], principled_bsdf_2.inputs[0])
    # voronoi_texture_001_1.Distance -> colorramp_002.Fac
    rockshader___3.links.new(voronoi_texture_001_1.outputs[0], colorramp_002.inputs[0])
    # mapping_001.Vector -> noise_texture_2.Vector
    rockshader___3.links.new(mapping_001.outputs[0], noise_texture_2.inputs[0])
    # noise_texture_2.Fac -> mix_1.B
    rockshader___3.links.new(noise_texture_2.outputs[0], mix_1.inputs[7])
    # mapping_001.Vector -> mix_1.A
    rockshader___3.links.new(mapping_001.outputs[0], mix_1.inputs[6])
    # voronoi_texture_001_1.Distance -> bump_2.Height
    rockshader___3.links.new(voronoi_texture_001_1.outputs[0], bump_2.inputs[2])
    # mix_1.Result -> voronoi_texture_001_1.Vector
    rockshader___3.links.new(mix_1.outputs[2], voronoi_texture_001_1.inputs[0])
    # colorramp_003.Color -> hue_saturation_value_2.Color
    rockshader___3.links.new(colorramp_003.outputs[0], hue_saturation_value_2.inputs[4])
    # mapping_2.Vector -> mapping_001.Vector
    rockshader___3.links.new(mapping_2.outputs[0], mapping_001.inputs[0])
    # voronoi_texture_2.Distance -> mix_001_2.Factor
    rockshader___3.links.new(voronoi_texture_2.outputs[0], mix_001_2.inputs[0])
    # voronoi_texture_001_1.Distance -> mix_001_2.B
    rockshader___3.links.new(voronoi_texture_001_1.outputs[0], mix_001_2.inputs[7])
    # colorramp.Color -> mix_002_1.Factor
    rockshader___3.links.new(colorramp.outputs[0], mix_002_1.inputs[0])
    # mix_001_2.Result -> colorramp.Fac
    rockshader___3.links.new(mix_001_2.outputs[2], colorramp.inputs[0])
    # bump_2.Normal -> bump_001_2.Normal
    rockshader___3.links.new(bump_2.outputs[0], bump_001_2.inputs[3])
    # mapping_001.Vector -> noise_texture_001_2.Vector
    rockshader___3.links.new(mapping_001.outputs[0], noise_texture_001_2.inputs[0])
    # noise_texture_001_2.Fac -> colorramp_001.Fac
    rockshader___3.links.new(noise_texture_001_2.outputs[0], colorramp_001.inputs[0])
    # mix_001_2.Result -> colorramp_003.Fac
    rockshader___3.links.new(mix_001_2.outputs[2], colorramp_003.inputs[0])
    # mix_002_1.Result -> mix_003_2.A
    rockshader___3.links.new(mix_002_1.outputs[2], mix_003_2.inputs[6])
    # colorramp_002.Color -> mix_004_1.Factor
    rockshader___3.links.new(colorramp_002.outputs[0], mix_004_1.inputs[0])
    # principled_bsdf_2.BSDF -> group_output_4.Shader
    rockshader___3.links.new(principled_bsdf_2.outputs[0], group_output_4.inputs[0])
    # group_input_4.Scale -> mapping_2.Scale
    rockshader___3.links.new(group_input_4.outputs[0], mapping_2.inputs[3])
    # group_input_4.Color 1 -> mix_002_1.A
    rockshader___3.links.new(group_input_4.outputs[1], mix_002_1.inputs[6])
    # group_input_4.Color 2 -> mix_002_1.B
    rockshader___3.links.new(group_input_4.outputs[2], mix_002_1.inputs[7])
    # group_input_4.Color 3 -> mix_003_2.B
    rockshader___3.links.new(group_input_4.outputs[3], mix_003_2.inputs[7])
    # group_input_4.Color 4 -> mix_004_1.B
    rockshader___3.links.new(group_input_4.outputs[4], mix_004_1.inputs[7])
    # group_input_4.Noise Scale -> noise_texture_2.Scale
    rockshader___3.links.new(group_input_4.outputs[5], noise_texture_2.inputs[2])
    # group_input_4.Chunks Scale -> voronoi_texture_001_1.Scale
    rockshader___3.links.new(group_input_4.outputs[6], voronoi_texture_001_1.inputs[2])
    # group_input_4.Noise Detail 1 -> noise_texture_2.Detail
    rockshader___3.links.new(group_input_4.outputs[7], noise_texture_2.inputs[3])
    # group_input_4.Distortion -> mix_1.Factor
    rockshader___3.links.new(group_input_4.outputs[9], mix_1.inputs[0])
    # group_input_4.Roughness -> hue_saturation_value_2.Value
    rockshader___3.links.new(
        group_input_4.outputs[10], hue_saturation_value_2.inputs[2]
    )
    # group_input_4.Noise Bump Strength -> bump_2.Strength
    rockshader___3.links.new(group_input_4.outputs[11], bump_2.inputs[0])
    # group_input_4.Detail Bump Strength -> bump_001_2.Strength
    rockshader___3.links.new(group_input_4.outputs[12], bump_001_2.inputs[0])
    # group_input_4.Noise Detail 2 -> clamp_1.Value
    rockshader___3.links.new(group_input_4.outputs[8], clamp_1.inputs[0])
    # clamp_1.Result -> noise_texture_2.Roughness
    rockshader___3.links.new(clamp_1.outputs[0], noise_texture_2.inputs[4])
    # group_001_2.0 -> map_range_011.Value
    rockshader___3.links.new(group_001_2.outputs[0], map_range_011.inputs[0])
    # map_range_011.Result -> mapping_2.Location
    rockshader___3.links.new(map_range_011.outputs[0], mapping_2.inputs[1])
    return rockshader___3


rockshader___3 = rockshader___3_node_group()


# initialize RockShader | 4 node group
def rockshader___4_node_group():
    rockshader___4 = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="RockShader | 4"
    )

    rockshader___4.color_tag = "NONE"
    rockshader___4.description = ""
    rockshader___4.default_group_node_width = 140

    # rockshader___4 interface
    # Socket Shader
    shader_socket_2 = rockshader___4.interface.new_socket(
        name="Shader", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    shader_socket_2.attribute_domain = "POINT"

    # Socket Scale
    scale_socket_3 = rockshader___4.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    scale_socket_3.default_value = 1.0
    scale_socket_3.min_value = -3.4028234663852886e38
    scale_socket_3.max_value = 3.4028234663852886e38
    scale_socket_3.subtype = "NONE"
    scale_socket_3.attribute_domain = "POINT"

    # Socket Color 1
    color_1_socket_1 = rockshader___4.interface.new_socket(
        name="Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_1_socket_1.default_value = (
        0.6590179800987244,
        0.24836499989032745,
        0.0748089998960495,
        1.0,
    )
    color_1_socket_1.attribute_domain = "POINT"

    # Socket Color 2
    color_2_socket_1 = rockshader___4.interface.new_socket(
        name="Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_2_socket_1.default_value = (
        0.07483299821615219,
        0.01208100002259016,
        0.006566000171005726,
        1.0,
    )
    color_2_socket_1.attribute_domain = "POINT"

    # Socket Color 3
    color_3_socket_1 = rockshader___4.interface.new_socket(
        name="Color 3", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_3_socket_1.default_value = (
        0.046142999082803726,
        0.007871000096201897,
        0.004050000105053186,
        1.0,
    )
    color_3_socket_1.attribute_domain = "POINT"

    # Socket Noise Scale
    noise_scale_socket_1 = rockshader___4.interface.new_socket(
        name="Noise Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_scale_socket_1.default_value = 18.0
    noise_scale_socket_1.min_value = -1000.0
    noise_scale_socket_1.max_value = 1000.0
    noise_scale_socket_1.subtype = "NONE"
    noise_scale_socket_1.attribute_domain = "POINT"

    # Socket Voronoi Scale
    voronoi_scale_socket = rockshader___4.interface.new_socket(
        name="Voronoi Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    voronoi_scale_socket.default_value = 16.0
    voronoi_scale_socket.min_value = -1000.0
    voronoi_scale_socket.max_value = 1000.0
    voronoi_scale_socket.subtype = "NONE"
    voronoi_scale_socket.attribute_domain = "POINT"

    # Socket Wave Scale
    wave_scale_socket = rockshader___4.interface.new_socket(
        name="Wave Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    wave_scale_socket.default_value = 6.0
    wave_scale_socket.min_value = -1000.0
    wave_scale_socket.max_value = 1000.0
    wave_scale_socket.subtype = "NONE"
    wave_scale_socket.attribute_domain = "POINT"

    # Socket Cracks Scale
    cracks_scale_socket = rockshader___4.interface.new_socket(
        name="Cracks Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    cracks_scale_socket.default_value = 4.0
    cracks_scale_socket.min_value = -1000.0
    cracks_scale_socket.max_value = 1000.0
    cracks_scale_socket.subtype = "NONE"
    cracks_scale_socket.attribute_domain = "POINT"

    # Socket Texture Detail
    texture_detail_socket = rockshader___4.interface.new_socket(
        name="Texture Detail", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    texture_detail_socket.default_value = 15.0
    texture_detail_socket.min_value = 0.0
    texture_detail_socket.max_value = 15.0
    texture_detail_socket.subtype = "NONE"
    texture_detail_socket.attribute_domain = "POINT"

    # Socket Roughness
    roughness_socket_3 = rockshader___4.interface.new_socket(
        name="Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    roughness_socket_3.default_value = 1.0
    roughness_socket_3.min_value = 0.0
    roughness_socket_3.max_value = 2.0
    roughness_socket_3.subtype = "NONE"
    roughness_socket_3.attribute_domain = "POINT"

    # Socket Noise Bump Strength
    noise_bump_strength_socket_1 = rockshader___4.interface.new_socket(
        name="Noise Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_bump_strength_socket_1.default_value = 0.10000000149011612
    noise_bump_strength_socket_1.min_value = 0.0
    noise_bump_strength_socket_1.max_value = 1.0
    noise_bump_strength_socket_1.subtype = "FACTOR"
    noise_bump_strength_socket_1.attribute_domain = "POINT"

    # Socket Cracks Bump Strength
    cracks_bump_strength_socket = rockshader___4.interface.new_socket(
        name="Cracks Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    cracks_bump_strength_socket.default_value = 0.6000000238418579
    cracks_bump_strength_socket.min_value = 0.0
    cracks_bump_strength_socket.max_value = 1.0
    cracks_bump_strength_socket.subtype = "FACTOR"
    cracks_bump_strength_socket.attribute_domain = "POINT"

    # Socket Strength
    strength_socket = rockshader___4.interface.new_socket(
        name="Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    strength_socket.default_value = 0.09132219105958939
    strength_socket.min_value = 0.0
    strength_socket.max_value = 1.0
    strength_socket.subtype = "FACTOR"
    strength_socket.attribute_domain = "POINT"

    # initialize rockshader___4 nodes
    # node Group Output
    group_output_5 = rockshader___4.nodes.new("NodeGroupOutput")
    group_output_5.name = "Group Output"
    group_output_5.is_active_output = True

    # node Texture Coordinate
    texture_coordinate_3 = rockshader___4.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_3.name = "Texture Coordinate"
    texture_coordinate_3.from_instancer = False

    # node Mapping
    mapping_3 = rockshader___4.nodes.new("ShaderNodeMapping")
    mapping_3.name = "Mapping"
    mapping_3.vector_type = "POINT"
    # Rotation
    mapping_3.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Mapping.001
    mapping_001_1 = rockshader___4.nodes.new("ShaderNodeMapping")
    mapping_001_1.name = "Mapping.001"
    mapping_001_1.vector_type = "POINT"
    # Location
    mapping_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    mapping_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    mapping_001_1.inputs[3].default_value = (1.0, 1.0, 1.399999976158142)

    # node Mix
    mix_2 = rockshader___4.nodes.new("ShaderNodeMix")
    mix_2.name = "Mix"
    mix_2.blend_type = "LINEAR_LIGHT"
    mix_2.clamp_factor = True
    mix_2.clamp_result = False
    mix_2.data_type = "RGBA"
    mix_2.factor_mode = "UNIFORM"
    # Factor_Float
    mix_2.inputs[0].default_value = 0.10000000149011612

    # node ColorRamp
    colorramp_1 = rockshader___4.nodes.new("ShaderNodeValToRGB")
    colorramp_1.name = "ColorRamp"
    colorramp_1.color_ramp.color_mode = "RGB"
    colorramp_1.color_ramp.hue_interpolation = "NEAR"
    colorramp_1.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_1.color_ramp.elements.remove(colorramp_1.color_ramp.elements[0])
    colorramp_1_cre_0 = colorramp_1.color_ramp.elements[0]
    colorramp_1_cre_0.position = 0.0
    colorramp_1_cre_0.alpha = 1.0
    colorramp_1_cre_0.color = (1.0, 1.0, 1.0, 1.0)

    colorramp_1_cre_1 = colorramp_1.color_ramp.elements.new(0.20822615921497345)
    colorramp_1_cre_1.alpha = 1.0
    colorramp_1_cre_1.color = (
        0.5014079809188843,
        0.5014079809188843,
        0.5014079809188843,
        1.0,
    )

    # node Principled BSDF
    principled_bsdf_3 = rockshader___4.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_3.name = "Principled BSDF"
    principled_bsdf_3.distribution = "GGX"
    principled_bsdf_3.subsurface_method = "RANDOM_WALK_SKIN"
    # Metallic
    principled_bsdf_3.inputs[1].default_value = 0.0
    # IOR
    principled_bsdf_3.inputs[3].default_value = 1.4500000476837158
    # Alpha
    principled_bsdf_3.inputs[4].default_value = 1.0
    # Diffuse Roughness
    principled_bsdf_3.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf_3.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf_3.inputs[9].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf_3.inputs[10].default_value = 0.05000000074505806
    # Subsurface IOR
    principled_bsdf_3.inputs[11].default_value = 1.399999976158142
    # Subsurface Anisotropy
    principled_bsdf_3.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf_3.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf_3.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf_3.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf_3.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf_3.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf_3.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf_3.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf_3.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf_3.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf_3.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf_3.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf_3.inputs[24].default_value = 0.0
    # Sheen Roughness
    principled_bsdf_3.inputs[25].default_value = 0.5
    # Sheen Tint
    principled_bsdf_3.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf_3.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
    # Emission Strength
    principled_bsdf_3.inputs[28].default_value = 1.0
    # Thin Film Thickness
    principled_bsdf_3.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf_3.inputs[30].default_value = 1.3300000429153442

    # node RGB Curves
    rgb_curves = rockshader___4.nodes.new("ShaderNodeRGBCurve")
    rgb_curves.name = "RGB Curves"
    # mapping settings
    rgb_curves.mapping.extend = "EXTRAPOLATED"
    rgb_curves.mapping.tone = "STANDARD"
    rgb_curves.mapping.black_level = (0.0, 0.0, 0.0)
    rgb_curves.mapping.white_level = (1.0, 1.0, 1.0)
    rgb_curves.mapping.clip_min_x = 0.0
    rgb_curves.mapping.clip_min_y = 0.0
    rgb_curves.mapping.clip_max_x = 1.0
    rgb_curves.mapping.clip_max_y = 1.0
    rgb_curves.mapping.use_clip = True
    # curve 0
    rgb_curves_curve_0 = rgb_curves.mapping.curves[0]
    rgb_curves_curve_0_point_0 = rgb_curves_curve_0.points[0]
    rgb_curves_curve_0_point_0.location = (0.0, 0.0)
    rgb_curves_curve_0_point_0.handle_type = "AUTO"
    rgb_curves_curve_0_point_1 = rgb_curves_curve_0.points[1]
    rgb_curves_curve_0_point_1.location = (1.0, 1.0)
    rgb_curves_curve_0_point_1.handle_type = "AUTO"
    # curve 1
    rgb_curves_curve_1 = rgb_curves.mapping.curves[1]
    rgb_curves_curve_1_point_0 = rgb_curves_curve_1.points[0]
    rgb_curves_curve_1_point_0.location = (0.0, 0.0)
    rgb_curves_curve_1_point_0.handle_type = "AUTO"
    rgb_curves_curve_1_point_1 = rgb_curves_curve_1.points[1]
    rgb_curves_curve_1_point_1.location = (1.0, 1.0)
    rgb_curves_curve_1_point_1.handle_type = "AUTO"
    # curve 2
    rgb_curves_curve_2 = rgb_curves.mapping.curves[2]
    rgb_curves_curve_2_point_0 = rgb_curves_curve_2.points[0]
    rgb_curves_curve_2_point_0.location = (0.0, 0.0)
    rgb_curves_curve_2_point_0.handle_type = "AUTO"
    rgb_curves_curve_2_point_1 = rgb_curves_curve_2.points[1]
    rgb_curves_curve_2_point_1.location = (1.0, 1.0)
    rgb_curves_curve_2_point_1.handle_type = "AUTO"
    # curve 3
    rgb_curves_curve_3 = rgb_curves.mapping.curves[3]
    rgb_curves_curve_3_point_0 = rgb_curves_curve_3.points[0]
    rgb_curves_curve_3_point_0.location = (0.0, 0.0)
    rgb_curves_curve_3_point_0.handle_type = "AUTO"
    rgb_curves_curve_3_point_1 = rgb_curves_curve_3.points[1]
    rgb_curves_curve_3_point_1.location = (0.2107970118522644, 0.2904413044452667)
    rgb_curves_curve_3_point_1.handle_type = "AUTO"
    rgb_curves_curve_3_point_2 = rgb_curves_curve_3.points.new(
        0.4678661823272705, 0.4007352888584137
    )
    rgb_curves_curve_3_point_2.handle_type = "AUTO"
    rgb_curves_curve_3_point_3 = rgb_curves_curve_3.points.new(
        0.5861183404922485, 0.7536765933036804
    )
    rgb_curves_curve_3_point_3.handle_type = "AUTO"
    rgb_curves_curve_3_point_4 = rgb_curves_curve_3.points.new(1.0, 1.0)
    rgb_curves_curve_3_point_4.handle_type = "AUTO"
    # update curve after changes
    rgb_curves.mapping.update()
    # Fac
    rgb_curves.inputs[0].default_value = 1.0

    # node Mix.001
    mix_001_3 = rockshader___4.nodes.new("ShaderNodeMix")
    mix_001_3.name = "Mix.001"
    mix_001_3.blend_type = "DARKEN"
    mix_001_3.clamp_factor = True
    mix_001_3.clamp_result = False
    mix_001_3.data_type = "RGBA"
    mix_001_3.factor_mode = "UNIFORM"
    # Factor_Float
    mix_001_3.inputs[0].default_value = 1.0

    # node ColorRamp.001
    colorramp_001_1 = rockshader___4.nodes.new("ShaderNodeValToRGB")
    colorramp_001_1.name = "ColorRamp.001"
    colorramp_001_1.color_ramp.color_mode = "RGB"
    colorramp_001_1.color_ramp.hue_interpolation = "NEAR"
    colorramp_001_1.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    colorramp_001_1.color_ramp.elements.remove(colorramp_001_1.color_ramp.elements[0])
    colorramp_001_1_cre_0 = colorramp_001_1.color_ramp.elements[0]
    colorramp_001_1_cre_0.position = 0.0
    colorramp_001_1_cre_0.alpha = 1.0
    colorramp_001_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_001_1_cre_1 = colorramp_001_1.color_ramp.elements.new(0.05912623554468155)
    colorramp_001_1_cre_1.alpha = 1.0
    colorramp_001_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node RGB Curves.001
    rgb_curves_001 = rockshader___4.nodes.new("ShaderNodeRGBCurve")
    rgb_curves_001.name = "RGB Curves.001"
    # mapping settings
    rgb_curves_001.mapping.extend = "EXTRAPOLATED"
    rgb_curves_001.mapping.tone = "STANDARD"
    rgb_curves_001.mapping.black_level = (0.0, 0.0, 0.0)
    rgb_curves_001.mapping.white_level = (1.0, 1.0, 1.0)
    rgb_curves_001.mapping.clip_min_x = 0.0
    rgb_curves_001.mapping.clip_min_y = 0.0
    rgb_curves_001.mapping.clip_max_x = 1.0
    rgb_curves_001.mapping.clip_max_y = 1.0
    rgb_curves_001.mapping.use_clip = True
    # curve 0
    rgb_curves_001_curve_0 = rgb_curves_001.mapping.curves[0]
    rgb_curves_001_curve_0_point_0 = rgb_curves_001_curve_0.points[0]
    rgb_curves_001_curve_0_point_0.location = (0.0, 0.0)
    rgb_curves_001_curve_0_point_0.handle_type = "AUTO"
    rgb_curves_001_curve_0_point_1 = rgb_curves_001_curve_0.points[1]
    rgb_curves_001_curve_0_point_1.location = (1.0, 1.0)
    rgb_curves_001_curve_0_point_1.handle_type = "AUTO"
    # curve 1
    rgb_curves_001_curve_1 = rgb_curves_001.mapping.curves[1]
    rgb_curves_001_curve_1_point_0 = rgb_curves_001_curve_1.points[0]
    rgb_curves_001_curve_1_point_0.location = (0.0, 0.0)
    rgb_curves_001_curve_1_point_0.handle_type = "AUTO"
    rgb_curves_001_curve_1_point_1 = rgb_curves_001_curve_1.points[1]
    rgb_curves_001_curve_1_point_1.location = (1.0, 1.0)
    rgb_curves_001_curve_1_point_1.handle_type = "AUTO"
    # curve 2
    rgb_curves_001_curve_2 = rgb_curves_001.mapping.curves[2]
    rgb_curves_001_curve_2_point_0 = rgb_curves_001_curve_2.points[0]
    rgb_curves_001_curve_2_point_0.location = (0.0, 0.0)
    rgb_curves_001_curve_2_point_0.handle_type = "AUTO"
    rgb_curves_001_curve_2_point_1 = rgb_curves_001_curve_2.points[1]
    rgb_curves_001_curve_2_point_1.location = (1.0, 1.0)
    rgb_curves_001_curve_2_point_1.handle_type = "AUTO"
    # curve 3
    rgb_curves_001_curve_3 = rgb_curves_001.mapping.curves[3]
    rgb_curves_001_curve_3_point_0 = rgb_curves_001_curve_3.points[0]
    rgb_curves_001_curve_3_point_0.location = (0.0, 0.0)
    rgb_curves_001_curve_3_point_0.handle_type = "AUTO"
    rgb_curves_001_curve_3_point_1 = rgb_curves_001_curve_3.points[1]
    rgb_curves_001_curve_3_point_1.location = (0.34961429238319397, 0.15073515474796295)
    rgb_curves_001_curve_3_point_1.handle_type = "AUTO"
    rgb_curves_001_curve_3_point_2 = rgb_curves_001_curve_3.points.new(
        0.6143959164619446, 0.764706015586853
    )
    rgb_curves_001_curve_3_point_2.handle_type = "AUTO"
    rgb_curves_001_curve_3_point_3 = rgb_curves_001_curve_3.points.new(1.0, 1.0)
    rgb_curves_001_curve_3_point_3.handle_type = "AUTO"
    # update curve after changes
    rgb_curves_001.mapping.update()
    # Fac
    rgb_curves_001.inputs[0].default_value = 1.0

    # node Mix.002
    mix_002_2 = rockshader___4.nodes.new("ShaderNodeMix")
    mix_002_2.name = "Mix.002"
    mix_002_2.blend_type = "MIX"
    mix_002_2.clamp_factor = True
    mix_002_2.clamp_result = False
    mix_002_2.data_type = "RGBA"
    mix_002_2.factor_mode = "UNIFORM"

    # node Mix.003
    mix_003_3 = rockshader___4.nodes.new("ShaderNodeMix")
    mix_003_3.name = "Mix.003"
    mix_003_3.blend_type = "MIX"
    mix_003_3.clamp_factor = True
    mix_003_3.clamp_result = False
    mix_003_3.data_type = "RGBA"
    mix_003_3.factor_mode = "UNIFORM"

    # node Voronoi Texture
    voronoi_texture_3 = rockshader___4.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_3.name = "Voronoi Texture"
    voronoi_texture_3.distance = "CHEBYCHEV"
    voronoi_texture_3.feature = "F1"
    voronoi_texture_3.normalize = False
    voronoi_texture_3.voronoi_dimensions = "3D"
    # Detail
    voronoi_texture_3.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_3.inputs[4].default_value = 0.5
    # Lacunarity
    voronoi_texture_3.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture_3.inputs[8].default_value = 1.0

    # node Wave Texture
    wave_texture = rockshader___4.nodes.new("ShaderNodeTexWave")
    wave_texture.name = "Wave Texture"
    wave_texture.bands_direction = "Z"
    wave_texture.rings_direction = "X"
    wave_texture.wave_profile = "SIN"
    wave_texture.wave_type = "BANDS"
    # Distortion
    wave_texture.inputs[2].default_value = 8.0
    # Detail Scale
    wave_texture.inputs[4].default_value = 2.0
    # Detail Roughness
    wave_texture.inputs[5].default_value = 0.6200000047683716
    # Phase Offset
    wave_texture.inputs[6].default_value = 0.0

    # node Noise Texture
    noise_texture_3 = rockshader___4.nodes.new("ShaderNodeTexNoise")
    noise_texture_3.name = "Noise Texture"
    noise_texture_3.noise_dimensions = "4D"
    noise_texture_3.noise_type = "FBM"
    noise_texture_3.normalize = True
    # W
    noise_texture_3.inputs[1].default_value = 0.0
    # Roughness
    noise_texture_3.inputs[4].default_value = 0.550000011920929
    # Lacunarity
    noise_texture_3.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_3.inputs[8].default_value = 0.0

    # node Wave Texture.001
    wave_texture_001 = rockshader___4.nodes.new("ShaderNodeTexWave")
    wave_texture_001.name = "Wave Texture.001"
    wave_texture_001.bands_direction = "Z"
    wave_texture_001.rings_direction = "X"
    wave_texture_001.wave_profile = "SIN"
    wave_texture_001.wave_type = "BANDS"
    # Distortion
    wave_texture_001.inputs[2].default_value = 20.0
    # Detail Scale
    wave_texture_001.inputs[4].default_value = 2.0
    # Detail Roughness
    wave_texture_001.inputs[5].default_value = 0.6200000047683716
    # Phase Offset
    wave_texture_001.inputs[6].default_value = 0.0

    # node Hue Saturation Value
    hue_saturation_value_3 = rockshader___4.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_3.name = "Hue Saturation Value"
    # Hue
    hue_saturation_value_3.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value_3.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value_3.inputs[3].default_value = 1.0

    # node Bump
    bump_3 = rockshader___4.nodes.new("ShaderNodeBump")
    bump_3.name = "Bump"
    bump_3.invert = False
    # Distance
    bump_3.inputs[1].default_value = 1.0
    # Normal
    bump_3.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Bump.001
    bump_001_3 = rockshader___4.nodes.new("ShaderNodeBump")
    bump_001_3.name = "Bump.001"
    bump_001_3.invert = False
    # Distance
    bump_001_3.inputs[1].default_value = 1.0

    # node Group Input
    group_input_5 = rockshader___4.nodes.new("NodeGroupInput")
    group_input_5.name = "Group Input"

    # node Map Range.011
    map_range_011_1 = rockshader___4.nodes.new("ShaderNodeMapRange")
    map_range_011_1.name = "Map Range.011"
    map_range_011_1.clamp = True
    map_range_011_1.data_type = "FLOAT"
    map_range_011_1.interpolation_type = "LINEAR"
    # From Min
    map_range_011_1.inputs[1].default_value = 0.0
    # From Max
    map_range_011_1.inputs[2].default_value = 1.0
    # To Min
    map_range_011_1.inputs[3].default_value = -1000.0
    # To Max
    map_range_011_1.inputs[4].default_value = 1000.0

    # node Group.001
    group_001_3 = rockshader___4.nodes.new("ShaderNodeGroup")
    group_001_3.name = "Group.001"
    group_001_3.node_tree = random_x2___mat
    # Socket_3
    group_001_3.inputs[0].default_value = 0.12449999898672104

    # node Bump.002
    bump_002_2 = rockshader___4.nodes.new("ShaderNodeBump")
    bump_002_2.name = "Bump.002"
    bump_002_2.invert = False
    # Distance
    bump_002_2.inputs[1].default_value = 1.0
    # Height
    bump_002_2.inputs[2].default_value = 1.0

    # Set locations
    group_output_5.location = (1435.3160400390625, 0.0)
    texture_coordinate_3.location = (-1245.31591796875, 66.28211975097656)
    mapping_3.location = (-1077.75537109375, 82.47952270507812)
    mapping_001_1.location = (-915.2177734375, 85.06170654296875)
    mix_2.location = (-578.0686645507812, 109.40525817871094)
    colorramp_1.location = (676.802978515625, 130.7415771484375)
    principled_bsdf_3.location = (1138.4149169921875, 346.54254150390625)
    rgb_curves.location = (-253.71597290039062, 427.0670166015625)
    mix_001_3.location = (78.52862548828125, 274.6394348144531)
    colorramp_001_1.location = (-553.4833984375, -227.36936950683594)
    rgb_curves_001.location = (-232.36538696289062, 97.50946044921875)
    mix_002_2.location = (303.08209228515625, 305.1787414550781)
    mix_003_3.location = (488.4228515625, 295.63385009765625)
    voronoi_texture_3.location = (-421.1315612792969, 115.88117980957031)
    wave_texture.location = (-747.1722412109375, 424.21881103515625)
    noise_texture_3.location = (-746.4063720703125, 85.30537414550781)
    wave_texture_001.location = (-748.0964965820312, -159.0817413330078)
    hue_saturation_value_3.location = (939.0760498046875, 123.91618347167969)
    bump_3.location = (292.3201904296875, -128.81381225585938)
    bump_001_3.location = (487.4517822265625, -126.61894226074219)
    group_input_5.location = (-1247.6279296875, -180.5272216796875)
    map_range_011_1.location = (-1488.3250732421875, -47.044227600097656)
    group_001_3.location = (-1670.5126953125, -198.06488037109375)
    bump_002_2.location = (694.7019653320312, -130.1945343017578)

    # initialize rockshader___4 links
    # mix_001_3.Result -> mix_002_2.Factor
    rockshader___4.links.new(mix_001_3.outputs[2], mix_002_2.inputs[0])
    # colorramp_001_1.Color -> bump_001_3.Height
    rockshader___4.links.new(colorramp_001_1.outputs[0], bump_001_3.inputs[2])
    # hue_saturation_value_3.Color -> principled_bsdf_3.Roughness
    rockshader___4.links.new(
        hue_saturation_value_3.outputs[0], principled_bsdf_3.inputs[2]
    )
    # mix_2.Result -> voronoi_texture_3.Vector
    rockshader___4.links.new(mix_2.outputs[2], voronoi_texture_3.inputs[0])
    # mix_003_3.Result -> principled_bsdf_3.Base Color
    rockshader___4.links.new(mix_003_3.outputs[2], principled_bsdf_3.inputs[0])
    # noise_texture_3.Color -> mix_2.B
    rockshader___4.links.new(noise_texture_3.outputs[1], mix_2.inputs[7])
    # bump_3.Normal -> bump_001_3.Normal
    rockshader___4.links.new(bump_3.outputs[0], bump_001_3.inputs[3])
    # colorramp_1.Color -> hue_saturation_value_3.Color
    rockshader___4.links.new(colorramp_1.outputs[0], hue_saturation_value_3.inputs[4])
    # mapping_001_1.Vector -> mix_2.A
    rockshader___4.links.new(mapping_001_1.outputs[0], mix_2.inputs[6])
    # noise_texture_3.Fac -> bump_3.Height
    rockshader___4.links.new(noise_texture_3.outputs[0], bump_3.inputs[2])
    # rgb_curves_001.Color -> mix_001_3.A
    rockshader___4.links.new(rgb_curves_001.outputs[0], mix_001_3.inputs[6])
    # voronoi_texture_3.Distance -> mix_003_3.Factor
    rockshader___4.links.new(voronoi_texture_3.outputs[0], mix_003_3.inputs[0])
    # mapping_001_1.Vector -> noise_texture_3.Vector
    rockshader___4.links.new(mapping_001_1.outputs[0], noise_texture_3.inputs[0])
    # mix_002_2.Result -> mix_003_3.A
    rockshader___4.links.new(mix_002_2.outputs[2], mix_003_3.inputs[6])
    # mapping_001_1.Vector -> wave_texture_001.Vector
    rockshader___4.links.new(mapping_001_1.outputs[0], wave_texture_001.inputs[0])
    # texture_coordinate_3.Object -> mapping_3.Vector
    rockshader___4.links.new(texture_coordinate_3.outputs[3], mapping_3.inputs[0])
    # wave_texture.Color -> rgb_curves.Color
    rockshader___4.links.new(wave_texture.outputs[0], rgb_curves.inputs[1])
    # voronoi_texture_3.Distance -> rgb_curves_001.Color
    rockshader___4.links.new(voronoi_texture_3.outputs[0], rgb_curves_001.inputs[1])
    # mix_003_3.Result -> colorramp_1.Fac
    rockshader___4.links.new(mix_003_3.outputs[2], colorramp_1.inputs[0])
    # mapping_001_1.Vector -> wave_texture.Vector
    rockshader___4.links.new(mapping_001_1.outputs[0], wave_texture.inputs[0])
    # mapping_3.Vector -> mapping_001_1.Vector
    rockshader___4.links.new(mapping_3.outputs[0], mapping_001_1.inputs[0])
    # rgb_curves.Color -> mix_001_3.B
    rockshader___4.links.new(rgb_curves.outputs[0], mix_001_3.inputs[7])
    # wave_texture_001.Color -> colorramp_001_1.Fac
    rockshader___4.links.new(wave_texture_001.outputs[0], colorramp_001_1.inputs[0])
    # principled_bsdf_3.BSDF -> group_output_5.Shader
    rockshader___4.links.new(principled_bsdf_3.outputs[0], group_output_5.inputs[0])
    # group_input_5.Scale -> mapping_3.Scale
    rockshader___4.links.new(group_input_5.outputs[0], mapping_3.inputs[3])
    # group_input_5.Color 1 -> mix_002_2.A
    rockshader___4.links.new(group_input_5.outputs[1], mix_002_2.inputs[6])
    # group_input_5.Color 2 -> mix_002_2.B
    rockshader___4.links.new(group_input_5.outputs[2], mix_002_2.inputs[7])
    # group_input_5.Color 3 -> mix_003_3.B
    rockshader___4.links.new(group_input_5.outputs[3], mix_003_3.inputs[7])
    # group_input_5.Noise Scale -> noise_texture_3.Scale
    rockshader___4.links.new(group_input_5.outputs[4], noise_texture_3.inputs[2])
    # group_input_5.Voronoi Scale -> voronoi_texture_3.Scale
    rockshader___4.links.new(group_input_5.outputs[5], voronoi_texture_3.inputs[2])
    # group_input_5.Wave Scale -> wave_texture.Scale
    rockshader___4.links.new(group_input_5.outputs[6], wave_texture.inputs[1])
    # group_input_5.Cracks Scale -> wave_texture_001.Scale
    rockshader___4.links.new(group_input_5.outputs[7], wave_texture_001.inputs[1])
    # group_input_5.Texture Detail -> wave_texture.Detail
    rockshader___4.links.new(group_input_5.outputs[8], wave_texture.inputs[3])
    # group_input_5.Texture Detail -> noise_texture_3.Detail
    rockshader___4.links.new(group_input_5.outputs[8], noise_texture_3.inputs[3])
    # group_input_5.Texture Detail -> wave_texture_001.Detail
    rockshader___4.links.new(group_input_5.outputs[8], wave_texture_001.inputs[3])
    # group_input_5.Roughness -> hue_saturation_value_3.Value
    rockshader___4.links.new(group_input_5.outputs[9], hue_saturation_value_3.inputs[2])
    # group_input_5.Noise Bump Strength -> bump_3.Strength
    rockshader___4.links.new(group_input_5.outputs[10], bump_3.inputs[0])
    # group_input_5.Cracks Bump Strength -> bump_001_3.Strength
    rockshader___4.links.new(group_input_5.outputs[11], bump_001_3.inputs[0])
    # group_001_3.0 -> map_range_011_1.Value
    rockshader___4.links.new(group_001_3.outputs[0], map_range_011_1.inputs[0])
    # map_range_011_1.Result -> mapping_3.Location
    rockshader___4.links.new(map_range_011_1.outputs[0], mapping_3.inputs[1])
    # bump_001_3.Normal -> bump_002_2.Normal
    rockshader___4.links.new(bump_001_3.outputs[0], bump_002_2.inputs[3])
    # bump_002_2.Normal -> principled_bsdf_3.Normal
    rockshader___4.links.new(bump_002_2.outputs[0], principled_bsdf_3.inputs[5])
    # group_input_5.Strength -> bump_002_2.Strength
    rockshader___4.links.new(group_input_5.outputs[12], bump_002_2.inputs[0])
    return rockshader___4


rockshader___4 = rockshader___4_node_group()


# initialize RockShader node group
def rockshader_node_group():
    rockshader = bpy.data.node_groups.new(type="ShaderNodeTree", name="RockShader")

    rockshader.color_tag = "NONE"
    rockshader.description = ""
    rockshader.default_group_node_width = 140

    # rockshader interface
    # Socket BSDF
    bsdf_socket_1 = rockshader.interface.new_socket(
        name="BSDF", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    bsdf_socket_1.attribute_domain = "POINT"

    # Socket Scale
    scale_socket_4 = rockshader.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    scale_socket_4.default_value = 1.0
    scale_socket_4.min_value = 0.0
    scale_socket_4.max_value = 3.4028234663852886e38
    scale_socket_4.subtype = "NONE"
    scale_socket_4.attribute_domain = "POINT"

    # Socket Rock Color 1
    rock_color_1_socket_1 = rockshader.interface.new_socket(
        name="Rock Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    rock_color_1_socket_1.default_value = (
        0.015996191650629044,
        0.015996308997273445,
        0.015996301546692848,
        1.0,
    )
    rock_color_1_socket_1.attribute_domain = "POINT"

    # Socket Rock Color 2
    rock_color_2_socket_1 = rockshader.interface.new_socket(
        name="Rock Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    rock_color_2_socket_1.default_value = (0.0, 0.0, 0.0, 1.0)
    rock_color_2_socket_1.attribute_domain = "POINT"

    # Socket Edge Lightness
    edge_lightness_socket = rockshader.interface.new_socket(
        name="Edge Lightness", in_out="INPUT", socket_type="NodeSocketColor"
    )
    edge_lightness_socket.default_value = (
        0.0998980849981308,
        0.0998988226056099,
        0.09989877790212631,
        1.0,
    )
    edge_lightness_socket.attribute_domain = "POINT"

    # Socket Noise Scale
    noise_scale_socket_2 = rockshader.interface.new_socket(
        name="Noise Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_scale_socket_2.default_value = 12.799999237060547
    noise_scale_socket_2.min_value = -1000.0
    noise_scale_socket_2.max_value = 1000.0
    noise_scale_socket_2.subtype = "NONE"
    noise_scale_socket_2.attribute_domain = "POINT"

    # Socket Noise Detail
    noise_detail_socket = rockshader.interface.new_socket(
        name="Noise Detail", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_detail_socket.default_value = 15.0
    noise_detail_socket.min_value = 0.0
    noise_detail_socket.max_value = 15.0
    noise_detail_socket.subtype = "NONE"
    noise_detail_socket.attribute_domain = "POINT"

    # Socket Noise Roughness
    noise_roughness_socket = rockshader.interface.new_socket(
        name="Noise Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_roughness_socket.default_value = 0.800000011920929
    noise_roughness_socket.min_value = 0.0
    noise_roughness_socket.max_value = 1.0
    noise_roughness_socket.subtype = "FACTOR"
    noise_roughness_socket.attribute_domain = "POINT"

    # Socket Light Noise Scale
    light_noise_scale_socket = rockshader.interface.new_socket(
        name="Light Noise Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    light_noise_scale_socket.default_value = 15.0
    light_noise_scale_socket.min_value = 0.0
    light_noise_scale_socket.max_value = 15.0
    light_noise_scale_socket.subtype = "NONE"
    light_noise_scale_socket.attribute_domain = "POINT"

    # Socket Light Roughness
    light_roughness_socket = rockshader.interface.new_socket(
        name="Light Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    light_roughness_socket.default_value = 0.5716666579246521
    light_roughness_socket.min_value = 0.0
    light_roughness_socket.max_value = 1.0
    light_roughness_socket.subtype = "FACTOR"
    light_roughness_socket.attribute_domain = "POINT"

    # Socket Rughness
    rughness_socket = rockshader.interface.new_socket(
        name="Rughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    rughness_socket.default_value = 1.0
    rughness_socket.min_value = 0.0
    rughness_socket.max_value = 2.0
    rughness_socket.subtype = "NONE"
    rughness_socket.attribute_domain = "POINT"

    # Socket Noise Bump Scale
    noise_bump_scale_socket = rockshader.interface.new_socket(
        name="Noise Bump Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_bump_scale_socket.default_value = 10.0
    noise_bump_scale_socket.min_value = -1000.0
    noise_bump_scale_socket.max_value = 1000.0
    noise_bump_scale_socket.subtype = "NONE"
    noise_bump_scale_socket.attribute_domain = "POINT"

    # Socket Noise Bump  Strength
    noise_bump__strength_socket = rockshader.interface.new_socket(
        name="Noise Bump  Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_bump__strength_socket.default_value = 0.20000000298023224
    noise_bump__strength_socket.min_value = 0.0
    noise_bump__strength_socket.max_value = 1.0
    noise_bump__strength_socket.subtype = "FACTOR"
    noise_bump__strength_socket.attribute_domain = "POINT"

    # Socket Detailed Noise Bump Strength
    detailed_noise_bump_strength_socket = rockshader.interface.new_socket(
        name="Detailed Noise Bump Strength",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
    )
    detailed_noise_bump_strength_socket.default_value = 0.30000001192092896
    detailed_noise_bump_strength_socket.min_value = 0.0
    detailed_noise_bump_strength_socket.max_value = 1.0
    detailed_noise_bump_strength_socket.subtype = "FACTOR"
    detailed_noise_bump_strength_socket.attribute_domain = "POINT"

    # Socket Edge Lightness strength
    edge_lightness_strength_socket = rockshader.interface.new_socket(
        name="Edge Lightness strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    edge_lightness_strength_socket.default_value = 0.4000000059604645
    edge_lightness_strength_socket.min_value = 0.0
    edge_lightness_strength_socket.max_value = 1.0
    edge_lightness_strength_socket.subtype = "FACTOR"
    edge_lightness_strength_socket.attribute_domain = "POINT"

    # Socket Noise scale mixer
    noise_scale_mixer_socket = rockshader.interface.new_socket(
        name="Noise scale mixer", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_scale_mixer_socket.default_value = 0.675000011920929
    noise_scale_mixer_socket.min_value = 0.0
    noise_scale_mixer_socket.max_value = 1.0
    noise_scale_mixer_socket.subtype = "FACTOR"
    noise_scale_mixer_socket.attribute_domain = "POINT"

    # Socket Noise Bump Roughness
    noise_bump_roughness_socket = rockshader.interface.new_socket(
        name="Noise Bump Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_bump_roughness_socket.default_value = 0.5
    noise_bump_roughness_socket.min_value = 0.0
    noise_bump_roughness_socket.max_value = 1.0
    noise_bump_roughness_socket.subtype = "FACTOR"
    noise_bump_roughness_socket.attribute_domain = "POINT"

    # Socket Voronoi Bump Scale
    voronoi_bump_scale_socket = rockshader.interface.new_socket(
        name="Voronoi Bump Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    voronoi_bump_scale_socket.default_value = 5.0
    voronoi_bump_scale_socket.min_value = -1000.0
    voronoi_bump_scale_socket.max_value = 1000.0
    voronoi_bump_scale_socket.subtype = "NONE"
    voronoi_bump_scale_socket.attribute_domain = "POINT"

    # Socket Voronoi Bump Strength
    voronoi_bump_strength_socket = rockshader.interface.new_socket(
        name="Voronoi Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    voronoi_bump_strength_socket.default_value = 1.0
    voronoi_bump_strength_socket.min_value = 0.0
    voronoi_bump_strength_socket.max_value = 1.0
    voronoi_bump_strength_socket.subtype = "FACTOR"
    voronoi_bump_strength_socket.attribute_domain = "POINT"

    # initialize rockshader nodes
    # node Group Output
    group_output_6 = rockshader.nodes.new("NodeGroupOutput")
    group_output_6.name = "Group Output"
    group_output_6.is_active_output = True

    # node Group Input
    group_input_6 = rockshader.nodes.new("NodeGroupInput")
    group_input_6.label = "Rock Color 2"
    group_input_6.name = "Group Input"

    # node Noise Texture
    noise_texture_4 = rockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_4.name = "Noise Texture"
    noise_texture_4.noise_dimensions = "4D"
    noise_texture_4.noise_type = "FBM"
    noise_texture_4.normalize = True
    # Lacunarity
    noise_texture_4.inputs[5].default_value = 20.0
    # Distortion
    noise_texture_4.inputs[8].default_value = 0.0

    # node Mapping.001
    mapping_001_2 = rockshader.nodes.new("ShaderNodeMapping")
    mapping_001_2.name = "Mapping.001"
    mapping_001_2.vector_type = "POINT"
    # Rotation
    mapping_001_2.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Texture Coordinate.001
    texture_coordinate_001 = rockshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False
    texture_coordinate_001.outputs[0].hide = True
    texture_coordinate_001.outputs[1].hide = True
    texture_coordinate_001.outputs[2].hide = True
    texture_coordinate_001.outputs[4].hide = True
    texture_coordinate_001.outputs[5].hide = True
    texture_coordinate_001.outputs[6].hide = True

    # node Bump
    bump_4 = rockshader.nodes.new("ShaderNodeBump")
    bump_4.name = "Bump"
    bump_4.invert = False
    # Distance
    bump_4.inputs[1].default_value = 1.0

    # node Color Ramp
    color_ramp_1 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_1.name = "Color Ramp"
    color_ramp_1.color_ramp.color_mode = "RGB"
    color_ramp_1.color_ramp.hue_interpolation = "NEAR"
    color_ramp_1.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_1.color_ramp.elements.remove(color_ramp_1.color_ramp.elements[0])
    color_ramp_1_cre_0 = color_ramp_1.color_ramp.elements[0]
    color_ramp_1_cre_0.position = 0.30181822180747986
    color_ramp_1_cre_0.alpha = 1.0
    color_ramp_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_1_cre_1 = color_ramp_1.color_ramp.elements.new(0.3945455849170685)
    color_ramp_1_cre_1.alpha = 1.0
    color_ramp_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Noise Texture.001
    noise_texture_001_3 = rockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001_3.name = "Noise Texture.001"
    noise_texture_001_3.noise_dimensions = "4D"
    noise_texture_001_3.noise_type = "FBM"
    noise_texture_001_3.normalize = True
    # Lacunarity
    noise_texture_001_3.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001_3.inputs[8].default_value = 0.0

    # node Color Ramp.001
    color_ramp_001_2 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001_2.name = "Color Ramp.001"
    color_ramp_001_2.color_ramp.color_mode = "RGB"
    color_ramp_001_2.color_ramp.hue_interpolation = "NEAR"
    color_ramp_001_2.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_001_2.color_ramp.elements.remove(color_ramp_001_2.color_ramp.elements[0])
    color_ramp_001_2_cre_0 = color_ramp_001_2.color_ramp.elements[0]
    color_ramp_001_2_cre_0.position = 0.4054546356201172
    color_ramp_001_2_cre_0.alpha = 1.0
    color_ramp_001_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_001_2_cre_1 = color_ramp_001_2.color_ramp.elements.new(0.64090895652771)
    color_ramp_001_2_cre_1.alpha = 1.0
    color_ramp_001_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Mix
    mix_3 = rockshader.nodes.new("ShaderNodeMix")
    mix_3.name = "Mix"
    mix_3.blend_type = "MIX"
    mix_3.clamp_factor = True
    mix_3.clamp_result = False
    mix_3.data_type = "RGBA"
    mix_3.factor_mode = "UNIFORM"

    # node Mix.001
    mix_001_4 = rockshader.nodes.new("ShaderNodeMix")
    mix_001_4.name = "Mix.001"
    mix_001_4.blend_type = "MIX"
    mix_001_4.clamp_factor = True
    mix_001_4.clamp_result = False
    mix_001_4.data_type = "RGBA"
    mix_001_4.factor_mode = "UNIFORM"

    # node Geometry
    geometry = rockshader.nodes.new("ShaderNodeNewGeometry")
    geometry.name = "Geometry"
    geometry.outputs[0].hide = True
    geometry.outputs[1].hide = True
    geometry.outputs[2].hide = True
    geometry.outputs[3].hide = True
    geometry.outputs[4].hide = True
    geometry.outputs[5].hide = True
    geometry.outputs[6].hide = True
    geometry.outputs[8].hide = True

    # node Color Ramp.002
    color_ramp_002_2 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_002_2.name = "Color Ramp.002"
    color_ramp_002_2.color_ramp.color_mode = "RGB"
    color_ramp_002_2.color_ramp.hue_interpolation = "NEAR"
    color_ramp_002_2.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp_002_2.color_ramp.elements.remove(color_ramp_002_2.color_ramp.elements[0])
    color_ramp_002_2_cre_0 = color_ramp_002_2.color_ramp.elements[0]
    color_ramp_002_2_cre_0.position = 0.5186362266540527
    color_ramp_002_2_cre_0.alpha = 1.0
    color_ramp_002_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_002_2_cre_1 = color_ramp_002_2.color_ramp.elements.new(
        0.6045457124710083
    )
    color_ramp_002_2_cre_1.alpha = 1.0
    color_ramp_002_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Mix.003
    mix_003_4 = rockshader.nodes.new("ShaderNodeMix")
    mix_003_4.name = "Mix.003"
    mix_003_4.blend_type = "MIX"
    mix_003_4.clamp_factor = True
    mix_003_4.clamp_result = False
    mix_003_4.data_type = "RGBA"
    mix_003_4.factor_mode = "UNIFORM"

    # node Color Ramp.004
    color_ramp_004_1 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004_1.name = "Color Ramp.004"
    color_ramp_004_1.color_ramp.color_mode = "RGB"
    color_ramp_004_1.color_ramp.hue_interpolation = "NEAR"
    color_ramp_004_1.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_004_1.color_ramp.elements.remove(color_ramp_004_1.color_ramp.elements[0])
    color_ramp_004_1_cre_0 = color_ramp_004_1.color_ramp.elements[0]
    color_ramp_004_1_cre_0.position = 0.0
    color_ramp_004_1_cre_0.alpha = 1.0
    color_ramp_004_1_cre_0.color = (
        0.6514015197753906,
        0.6514063477516174,
        0.6514060497283936,
        1.0,
    )

    color_ramp_004_1_cre_1 = color_ramp_004_1.color_ramp.elements.new(1.0)
    color_ramp_004_1_cre_1.alpha = 1.0
    color_ramp_004_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Noise Texture.003
    noise_texture_003_1 = rockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003_1.name = "Noise Texture.003"
    noise_texture_003_1.noise_dimensions = "4D"
    noise_texture_003_1.noise_type = "FBM"
    noise_texture_003_1.normalize = True
    # Detail
    noise_texture_003_1.inputs[3].default_value = 15.0
    # Lacunarity
    noise_texture_003_1.inputs[5].default_value = 0.0
    # Distortion
    noise_texture_003_1.inputs[8].default_value = 0.0

    # node Bump.001
    bump_001_4 = rockshader.nodes.new("ShaderNodeBump")
    bump_001_4.name = "Bump.001"
    bump_001_4.invert = False
    # Distance
    bump_001_4.inputs[1].default_value = 1.0

    # node Frame.001
    frame_001_1 = rockshader.nodes.new("NodeFrame")
    frame_001_1.name = "Frame.001"
    frame_001_1.label_size = 20
    frame_001_1.shrink = True

    # node Frame.002
    frame_002_1 = rockshader.nodes.new("NodeFrame")
    frame_002_1.name = "Frame.002"
    frame_002_1.label_size = 20
    frame_002_1.shrink = True

    # node Frame
    frame_1 = rockshader.nodes.new("NodeFrame")
    frame_1.name = "Frame"
    frame_1.label_size = 20
    frame_1.shrink = True

    # node Hue/Saturation/Value
    hue_saturation_value_4 = rockshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_4.name = "Hue/Saturation/Value"
    # Hue
    hue_saturation_value_4.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value_4.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value_4.inputs[3].default_value = 1.0

    # node Frame.003
    frame_003_1 = rockshader.nodes.new("NodeFrame")
    frame_003_1.name = "Frame.003"
    frame_003_1.label_size = 20
    frame_003_1.shrink = True

    # node Principled BSDF
    principled_bsdf_4 = rockshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_4.name = "Principled BSDF"
    principled_bsdf_4.distribution = "MULTI_GGX"
    principled_bsdf_4.subsurface_method = "RANDOM_WALK"
    # Metallic
    principled_bsdf_4.inputs[1].default_value = 0.0
    # IOR
    principled_bsdf_4.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf_4.inputs[4].default_value = 1.0
    # Diffuse Roughness
    principled_bsdf_4.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf_4.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf_4.inputs[9].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf_4.inputs[10].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf_4.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf_4.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf_4.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf_4.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf_4.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf_4.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf_4.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf_4.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf_4.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf_4.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf_4.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf_4.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf_4.inputs[24].default_value = 0.0
    # Sheen Roughness
    principled_bsdf_4.inputs[25].default_value = 0.5
    # Sheen Tint
    principled_bsdf_4.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf_4.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf_4.inputs[28].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf_4.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf_4.inputs[30].default_value = 1.3300000429153442

    # node Math
    math_3 = rockshader.nodes.new("ShaderNodeMath")
    math_3.name = "Math"
    math_3.operation = "MULTIPLY"
    math_3.use_clamp = False
    # Value_001
    math_3.inputs[1].default_value = 10.0

    # node Group.001
    group_001_4 = rockshader.nodes.new("ShaderNodeGroup")
    group_001_4.name = "Group.001"
    group_001_4.node_tree = random_x4___mat
    # Socket_5
    group_001_4.inputs[0].default_value = 0.5213124752044678

    # node Voronoi Texture
    voronoi_texture_4 = rockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_4.name = "Voronoi Texture"
    voronoi_texture_4.distance = "EUCLIDEAN"
    voronoi_texture_4.feature = "F1"
    voronoi_texture_4.normalize = True
    voronoi_texture_4.voronoi_dimensions = "4D"
    # Detail
    voronoi_texture_4.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_4.inputs[4].default_value = 1.0
    # Lacunarity
    voronoi_texture_4.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture_4.inputs[8].default_value = 1.0

    # node Bump.002
    bump_002_3 = rockshader.nodes.new("ShaderNodeBump")
    bump_002_3.name = "Bump.002"
    bump_002_3.invert = False
    # Distance
    bump_002_3.inputs[1].default_value = 1.0

    # node Color Ramp.005
    color_ramp_005_1 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005_1.name = "Color Ramp.005"
    color_ramp_005_1.color_ramp.color_mode = "RGB"
    color_ramp_005_1.color_ramp.hue_interpolation = "NEAR"
    color_ramp_005_1.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp_005_1.color_ramp.elements.remove(color_ramp_005_1.color_ramp.elements[0])
    color_ramp_005_1_cre_0 = color_ramp_005_1.color_ramp.elements[0]
    color_ramp_005_1_cre_0.position = 0.0
    color_ramp_005_1_cre_0.alpha = 1.0
    color_ramp_005_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_005_1_cre_1 = color_ramp_005_1.color_ramp.elements.new(
        0.15909108519554138
    )
    color_ramp_005_1_cre_1.alpha = 1.0
    color_ramp_005_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Voronoi Texture.001
    voronoi_texture_001_2 = rockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001_2.name = "Voronoi Texture.001"
    voronoi_texture_001_2.distance = "EUCLIDEAN"
    voronoi_texture_001_2.feature = "SMOOTH_F1"
    voronoi_texture_001_2.normalize = True
    voronoi_texture_001_2.voronoi_dimensions = "4D"
    # Detail
    voronoi_texture_001_2.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_001_2.inputs[4].default_value = 1.0
    # Lacunarity
    voronoi_texture_001_2.inputs[5].default_value = 2.0
    # Smoothness
    voronoi_texture_001_2.inputs[6].default_value = 1.0
    # Randomness
    voronoi_texture_001_2.inputs[8].default_value = 1.0

    # node Color Ramp.006
    color_ramp_006_1 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006_1.name = "Color Ramp.006"
    color_ramp_006_1.color_ramp.color_mode = "RGB"
    color_ramp_006_1.color_ramp.hue_interpolation = "NEAR"
    color_ramp_006_1.color_ramp.interpolation = "CARDINAL"

    # initialize color ramp elements
    color_ramp_006_1.color_ramp.elements.remove(color_ramp_006_1.color_ramp.elements[0])
    color_ramp_006_1_cre_0 = color_ramp_006_1.color_ramp.elements[0]
    color_ramp_006_1_cre_0.position = 0.0
    color_ramp_006_1_cre_0.alpha = 1.0
    color_ramp_006_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_006_1_cre_1 = color_ramp_006_1.color_ramp.elements.new(
        0.13181859254837036
    )
    color_ramp_006_1_cre_1.alpha = 1.0
    color_ramp_006_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Math.001
    math_001_1 = rockshader.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = "DIVIDE"
    math_001_1.use_clamp = False

    # node Bump.003
    bump_003_1 = rockshader.nodes.new("ShaderNodeBump")
    bump_003_1.name = "Bump.003"
    bump_003_1.invert = False
    # Distance
    bump_003_1.inputs[1].default_value = 1.0
    # Normal
    bump_003_1.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Map Range.004
    map_range_004_2 = rockshader.nodes.new("ShaderNodeMapRange")
    map_range_004_2.name = "Map Range.004"
    map_range_004_2.clamp = True
    map_range_004_2.data_type = "FLOAT"
    map_range_004_2.interpolation_type = "LINEAR"
    # From Min
    map_range_004_2.inputs[1].default_value = 0.0
    # From Max
    map_range_004_2.inputs[2].default_value = 1.0
    # To Min
    map_range_004_2.inputs[3].default_value = -1000.0
    # To Max
    map_range_004_2.inputs[4].default_value = 1000.0

    # node Group.002
    group_002 = rockshader.nodes.new("ShaderNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random_x4___mat

    # node Math.002
    math_002 = rockshader.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = "MULTIPLY"
    math_002.use_clamp = False

    # node Math.003
    math_003 = rockshader.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = "MULTIPLY"
    math_003.use_clamp = False
    # Value_001
    math_003.inputs[1].default_value = 5.0

    # node Math.004
    math_004 = rockshader.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = "MULTIPLY"
    math_004.use_clamp = False

    # Set parents
    noise_texture_4.parent = frame_1
    color_ramp_1.parent = frame_1
    noise_texture_001_3.parent = frame_1
    color_ramp_001_2.parent = frame_1
    mix_3.parent = frame_1
    mix_001_4.parent = frame_002_1
    geometry.parent = frame_001_1
    color_ramp_002_2.parent = frame_001_1
    mix_003_4.parent = frame_002_1
    color_ramp_004_1.parent = frame_003_1
    hue_saturation_value_4.parent = frame_003_1

    # Set locations
    group_output_6.location = (2044.083740234375, -366.00262451171875)
    group_input_6.location = (-1756.011962890625, -822.6982421875)
    noise_texture_4.location = (-3084.742431640625, 781.9205322265625)
    mapping_001_2.location = (-1281.65478515625, -227.8770751953125)
    texture_coordinate_001.location = (-1471.65478515625, -236.3770751953125)
    bump_4.location = (1154.56298828125, -790.7999267578125)
    color_ramp_1.location = (-2845.918701171875, 769.3270263671875)
    noise_texture_001_3.location = (-3091.82958984375, 348.28857421875)
    color_ramp_001_2.location = (-2840.2607421875, 369.6982421875)
    mix_3.location = (-2463.6015625, 642.8758544921875)
    mix_001_4.location = (-1338.03955078125, 856.2105102539062)
    geometry.location = (-1595.263427734375, 1377.4110107421875)
    color_ramp_002_2.location = (-1332.5478515625, 1497.3221435546875)
    mix_003_4.location = (-1139.2666015625, 857.9177856445312)
    color_ramp_004_1.location = (-1898.9849853515625, 572.5324096679688)
    noise_texture_003_1.location = (233.37887573242188, -895.6905517578125)
    bump_001_4.location = (1390.9708251953125, -663.4024658203125)
    frame_001_1.location = (1076.4444580078125, -1275.853271484375)
    frame_002_1.location = (1587.0386962890625, -923.2500610351562)
    frame_1.location = (2204.56005859375, -1019.8477783203125)
    hue_saturation_value_4.location = (-1571.6060791015625, 569.7412719726562)
    frame_003_1.location = (2145.8759765625, -1014.9539794921875)
    principled_bsdf_4.location = (1568.39306640625, -416.8108215332031)
    math_3.location = (-1059.811279296875, -390.11346435546875)
    group_001_4.location = (-2127.677001953125, -45.7719612121582)
    voronoi_texture_4.location = (201.54551696777344, -1322.15673828125)
    bump_002_3.location = (925.5811157226562, -915.0869750976562)
    color_ramp_005_1.location = (387.2950439453125, -1225.90478515625)
    voronoi_texture_001_2.location = (209.61325073242188, -1741.732666015625)
    color_ramp_006_1.location = (464.92108154296875, -1571.82275390625)
    math_001_1.location = (-162.15603637695312, -1974.9114990234375)
    bump_003_1.location = (761.9248046875, -1172.5350341796875)
    map_range_004_2.location = (-1697.904541015625, -193.53184509277344)
    group_002.location = (-1084.7215576171875, -1829.677734375)
    math_002.location = (-578.4093627929688, -1308.6357421875)
    math_003.location = (-452.7193603515625, -1984.625732421875)
    math_004.location = (-351.4325866699219, -1473.386962890625)

    # initialize rockshader links
    # mapping_001_2.Vector -> noise_texture_001_3.Vector
    rockshader.links.new(mapping_001_2.outputs[0], noise_texture_001_3.inputs[0])
    # noise_texture_001_3.Fac -> color_ramp_001_2.Fac
    rockshader.links.new(noise_texture_001_3.outputs[0], color_ramp_001_2.inputs[0])
    # color_ramp_001_2.Color -> mix_3.B
    rockshader.links.new(color_ramp_001_2.outputs[0], mix_3.inputs[7])
    # color_ramp_004_1.Color -> hue_saturation_value_4.Color
    rockshader.links.new(color_ramp_004_1.outputs[0], hue_saturation_value_4.inputs[4])
    # mix_001_4.Result -> mix_003_4.A
    rockshader.links.new(mix_001_4.outputs[2], mix_003_4.inputs[6])
    # mix_003_4.Result -> principled_bsdf_4.Base Color
    rockshader.links.new(mix_003_4.outputs[2], principled_bsdf_4.inputs[0])
    # color_ramp_002_2.Color -> mix_003_4.Factor
    rockshader.links.new(color_ramp_002_2.outputs[0], mix_003_4.inputs[0])
    # hue_saturation_value_4.Color -> principled_bsdf_4.Roughness
    rockshader.links.new(hue_saturation_value_4.outputs[0], principled_bsdf_4.inputs[2])
    # color_ramp_1.Color -> mix_3.A
    rockshader.links.new(color_ramp_1.outputs[0], mix_3.inputs[6])
    # mix_3.Result -> color_ramp_004_1.Fac
    rockshader.links.new(mix_3.outputs[2], color_ramp_004_1.inputs[0])
    # mapping_001_2.Vector -> noise_texture_003_1.Vector
    rockshader.links.new(mapping_001_2.outputs[0], noise_texture_003_1.inputs[0])
    # bump_4.Normal -> bump_001_4.Normal
    rockshader.links.new(bump_4.outputs[0], bump_001_4.inputs[3])
    # mix_3.Result -> mix_001_4.Factor
    rockshader.links.new(mix_3.outputs[2], mix_001_4.inputs[0])
    # mapping_001_2.Vector -> noise_texture_4.Vector
    rockshader.links.new(mapping_001_2.outputs[0], noise_texture_4.inputs[0])
    # geometry.Pointiness -> color_ramp_002_2.Fac
    rockshader.links.new(geometry.outputs[7], color_ramp_002_2.inputs[0])
    # mix_3.Result -> bump_001_4.Height
    rockshader.links.new(mix_3.outputs[2], bump_001_4.inputs[2])
    # noise_texture_4.Fac -> color_ramp_1.Fac
    rockshader.links.new(noise_texture_4.outputs[0], color_ramp_1.inputs[0])
    # texture_coordinate_001.Object -> mapping_001_2.Vector
    rockshader.links.new(texture_coordinate_001.outputs[3], mapping_001_2.inputs[0])
    # principled_bsdf_4.BSDF -> group_output_6.BSDF
    rockshader.links.new(principled_bsdf_4.outputs[0], group_output_6.inputs[0])
    # group_input_6.Scale -> mapping_001_2.Scale
    rockshader.links.new(group_input_6.outputs[0], mapping_001_2.inputs[3])
    # group_input_6.Rock Color 1 -> mix_001_4.A
    rockshader.links.new(group_input_6.outputs[1], mix_001_4.inputs[6])
    # group_input_6.Rock Color 2 -> mix_001_4.B
    rockshader.links.new(group_input_6.outputs[2], mix_001_4.inputs[7])
    # group_input_6.Edge Lightness -> mix_003_4.B
    rockshader.links.new(group_input_6.outputs[3], mix_003_4.inputs[7])
    # group_input_6.Noise Detail -> noise_texture_4.Detail
    rockshader.links.new(group_input_6.outputs[5], noise_texture_4.inputs[3])
    # group_input_6.Noise Roughness -> noise_texture_4.Roughness
    rockshader.links.new(group_input_6.outputs[6], noise_texture_4.inputs[4])
    # group_input_6.Noise Detail -> noise_texture_001_3.Detail
    rockshader.links.new(group_input_6.outputs[5], noise_texture_001_3.inputs[3])
    # group_input_6.Noise Roughness -> noise_texture_001_3.Roughness
    rockshader.links.new(group_input_6.outputs[6], noise_texture_001_3.inputs[4])
    # group_input_6.Rughness -> hue_saturation_value_4.Value
    rockshader.links.new(group_input_6.outputs[9], hue_saturation_value_4.inputs[2])
    # group_input_6.Noise Bump  Strength -> bump_4.Strength
    rockshader.links.new(group_input_6.outputs[11], bump_4.inputs[0])
    # group_input_6.Noise Bump Scale -> noise_texture_003_1.Scale
    rockshader.links.new(group_input_6.outputs[10], noise_texture_003_1.inputs[2])
    # group_input_6.Detailed Noise Bump Strength -> bump_001_4.Strength
    rockshader.links.new(group_input_6.outputs[12], bump_001_4.inputs[0])
    # group_input_6.Noise Scale -> noise_texture_001_3.Scale
    rockshader.links.new(group_input_6.outputs[4], noise_texture_001_3.inputs[2])
    # group_input_6.Noise scale mixer -> mix_3.Factor
    rockshader.links.new(group_input_6.outputs[14], mix_3.inputs[0])
    # group_input_6.Noise Scale -> math_3.Value
    rockshader.links.new(group_input_6.outputs[4], math_3.inputs[0])
    # math_3.Value -> noise_texture_4.Scale
    rockshader.links.new(math_3.outputs[0], noise_texture_4.inputs[2])
    # group_input_6.Noise Bump Roughness -> noise_texture_003_1.Roughness
    rockshader.links.new(group_input_6.outputs[15], noise_texture_003_1.inputs[4])
    # group_001_4.4 -> noise_texture_001_3.W
    rockshader.links.new(group_001_4.outputs[4], noise_texture_001_3.inputs[1])
    # group_001_4.3 -> noise_texture_4.W
    rockshader.links.new(group_001_4.outputs[3], noise_texture_4.inputs[1])
    # group_001_4.1 -> noise_texture_003_1.W
    rockshader.links.new(group_001_4.outputs[1], noise_texture_003_1.inputs[1])
    # bump_001_4.Normal -> principled_bsdf_4.Normal
    rockshader.links.new(bump_001_4.outputs[0], principled_bsdf_4.inputs[5])
    # noise_texture_003_1.Fac -> bump_4.Height
    rockshader.links.new(noise_texture_003_1.outputs[0], bump_4.inputs[2])
    # mapping_001_2.Vector -> voronoi_texture_4.Vector
    rockshader.links.new(mapping_001_2.outputs[0], voronoi_texture_4.inputs[0])
    # group_001_4.1 -> voronoi_texture_4.W
    rockshader.links.new(group_001_4.outputs[1], voronoi_texture_4.inputs[1])
    # color_ramp_005_1.Color -> bump_002_3.Height
    rockshader.links.new(color_ramp_005_1.outputs[0], bump_002_3.inputs[2])
    # bump_002_3.Normal -> bump_4.Normal
    rockshader.links.new(bump_002_3.outputs[0], bump_4.inputs[3])
    # voronoi_texture_4.Distance -> color_ramp_005_1.Fac
    rockshader.links.new(voronoi_texture_4.outputs[0], color_ramp_005_1.inputs[0])
    # group_input_6.Voronoi Bump Scale -> voronoi_texture_4.Scale
    rockshader.links.new(group_input_6.outputs[16], voronoi_texture_4.inputs[2])
    # mapping_001_2.Vector -> voronoi_texture_001_2.Vector
    rockshader.links.new(mapping_001_2.outputs[0], voronoi_texture_001_2.inputs[0])
    # group_001_4.1 -> voronoi_texture_001_2.W
    rockshader.links.new(group_001_4.outputs[1], voronoi_texture_001_2.inputs[1])
    # math_001_1.Value -> voronoi_texture_001_2.Scale
    rockshader.links.new(math_001_1.outputs[0], voronoi_texture_001_2.inputs[2])
    # voronoi_texture_001_2.Distance -> color_ramp_006_1.Fac
    rockshader.links.new(voronoi_texture_001_2.outputs[0], color_ramp_006_1.inputs[0])
    # group_input_6.Voronoi Bump Scale -> math_001_1.Value
    rockshader.links.new(group_input_6.outputs[16], math_001_1.inputs[0])
    # color_ramp_006_1.Color -> bump_003_1.Height
    rockshader.links.new(color_ramp_006_1.outputs[0], bump_003_1.inputs[2])
    # bump_003_1.Normal -> bump_002_3.Normal
    rockshader.links.new(bump_003_1.outputs[0], bump_002_3.inputs[3])
    # map_range_004_2.Result -> mapping_001_2.Location
    rockshader.links.new(map_range_004_2.outputs[0], mapping_001_2.inputs[1])
    # group_001_4.0 -> map_range_004_2.Value
    rockshader.links.new(group_001_4.outputs[0], map_range_004_2.inputs[0])
    # group_002.0 -> math_002.Value
    rockshader.links.new(group_002.outputs[0], math_002.inputs[1])
    # group_input_6.Voronoi Bump Strength -> math_002.Value
    rockshader.links.new(group_input_6.outputs[17], math_002.inputs[0])
    # math_002.Value -> bump_003_1.Strength
    rockshader.links.new(math_002.outputs[0], bump_003_1.inputs[0])
    # group_001_4.2 -> group_002.Seed
    rockshader.links.new(group_001_4.outputs[2], group_002.inputs[0])
    # math_003.Value -> math_001_1.Value
    rockshader.links.new(math_003.outputs[0], math_001_1.inputs[1])
    # group_002.1 -> math_003.Value
    rockshader.links.new(group_002.outputs[1], math_003.inputs[0])
    # group_input_6.Voronoi Bump Strength -> math_004.Value
    rockshader.links.new(group_input_6.outputs[17], math_004.inputs[0])
    # group_002.2 -> math_004.Value
    rockshader.links.new(group_002.outputs[2], math_004.inputs[1])
    # math_004.Value -> bump_002_3.Strength
    rockshader.links.new(math_004.outputs[0], bump_002_3.inputs[0])
    return rockshader


rockshader = rockshader_node_group()


# initialize MartianRockShader node group
def martianrockshader_node_group():
    martianrockshader = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="MartianRockShader"
    )

    martianrockshader.color_tag = "NONE"
    martianrockshader.description = ""
    martianrockshader.default_group_node_width = 140

    # martianrockshader interface
    # Socket Shader
    shader_socket_3 = martianrockshader.interface.new_socket(
        name="Shader", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    shader_socket_3.attribute_domain = "POINT"

    # initialize martianrockshader nodes
    # node Group Output
    group_output_7 = martianrockshader.nodes.new("NodeGroupOutput")
    group_output_7.name = "Group Output"
    group_output_7.is_active_output = True

    # node Group.005
    group_005 = martianrockshader.nodes.new("ShaderNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = rockshader___3
    # Input_2
    group_005.inputs[0].default_value = 1.0
    # Input_7
    group_005.inputs[5].default_value = 17.600000381469727
    # Input_8
    group_005.inputs[6].default_value = 2.7400002479553223
    # Input_9
    group_005.inputs[7].default_value = 15.0
    # Input_10
    group_005.inputs[8].default_value = 0.6979339122772217
    # Input_11
    group_005.inputs[9].default_value = 0.3623966872692108
    # Input_12
    group_005.inputs[10].default_value = 2.0
    # Input_13
    group_005.inputs[11].default_value = 0.43471091985702515
    # Input_14
    group_005.inputs[12].default_value = 0.2264467179775238

    # node Group.006
    group_006 = martianrockshader.nodes.new("ShaderNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = rockshader___4
    # Input_2
    group_006.inputs[0].default_value = 1.0
    # Input_6
    group_006.inputs[4].default_value = 18.68000030517578
    # Input_7
    group_006.inputs[5].default_value = 3.840001106262207
    # Input_8
    group_006.inputs[6].default_value = 4.180000305175781
    # Input_9
    group_006.inputs[7].default_value = 0.010000094771385193
    # Input_10
    group_006.inputs[8].default_value = 15.0
    # Input_11
    group_006.inputs[9].default_value = 2.0
    # Input_12
    group_006.inputs[10].default_value = 0.3370434641838074
    # Input_13
    group_006.inputs[11].default_value = 0.931240439414978
    # Socket_0
    group_006.inputs[12].default_value = 0.19363099336624146

    # node Combine Color.001
    combine_color_001 = martianrockshader.nodes.new("ShaderNodeCombineColor")
    combine_color_001.name = "Combine Color.001"
    combine_color_001.mode = "HSV"
    # Red
    combine_color_001.inputs[0].default_value = 0.029999999329447746
    # Green
    combine_color_001.inputs[1].default_value = 0.8999999761581421

    # node Map Range.005
    map_range_005 = martianrockshader.nodes.new("ShaderNodeMapRange")
    map_range_005.name = "Map Range.005"
    map_range_005.clamp = True
    map_range_005.data_type = "FLOAT"
    map_range_005.interpolation_type = "LINEAR"
    # From Min
    map_range_005.inputs[1].default_value = 0.0
    # From Max
    map_range_005.inputs[2].default_value = 1.0
    # To Min
    map_range_005.inputs[3].default_value = 0.05000000074505806
    # To Max
    map_range_005.inputs[4].default_value = 0.30000001192092896

    # node Combine Color.002
    combine_color_002 = martianrockshader.nodes.new("ShaderNodeCombineColor")
    combine_color_002.name = "Combine Color.002"
    combine_color_002.mode = "HSV"
    # Red
    combine_color_002.inputs[0].default_value = 0.021490026265382767
    # Green
    combine_color_002.inputs[1].default_value = 0.800000011920929

    # node Map Range.006
    map_range_006 = martianrockshader.nodes.new("ShaderNodeMapRange")
    map_range_006.name = "Map Range.006"
    map_range_006.clamp = True
    map_range_006.data_type = "FLOAT"
    map_range_006.interpolation_type = "LINEAR"
    # From Min
    map_range_006.inputs[1].default_value = 0.0
    # From Max
    map_range_006.inputs[2].default_value = 1.0
    # To Min
    map_range_006.inputs[3].default_value = 0.009999999776482582
    # To Max
    map_range_006.inputs[4].default_value = 0.019999999552965164

    # node Group.008
    group_008 = martianrockshader.nodes.new("ShaderNodeGroup")
    group_008.name = "Group.008"
    group_008.node_tree = rockshader
    # Socket_1
    group_008.inputs[0].default_value = 1.5
    # Socket_5
    group_008.inputs[4].default_value = 11.029998779296875
    # Socket_6
    group_008.inputs[5].default_value = 15.0
    # Socket_7
    group_008.inputs[6].default_value = 0.6499999761581421
    # Socket_8
    group_008.inputs[7].default_value = 8.320000648498535
    # Socket_9
    group_008.inputs[8].default_value = 0.7736417055130005
    # Socket_10
    group_008.inputs[9].default_value = 2.0
    # Socket_11
    group_008.inputs[10].default_value = 17.369998931884766
    # Socket_12
    group_008.inputs[11].default_value = 0.16358695924282074
    # Socket_13
    group_008.inputs[12].default_value = 0.3608698546886444
    # Socket_14
    group_008.inputs[13].default_value = 0.5271739959716797
    # Socket_16
    group_008.inputs[15].default_value = 0.2190222144126892
    # Socket_17
    group_008.inputs[16].default_value = 15.0
    # Socket_18
    group_008.inputs[17].default_value = 0.2663043737411499

    # node Mix Shader.001
    mix_shader_001 = martianrockshader.nodes.new("ShaderNodeMixShader")
    mix_shader_001.name = "Mix Shader.001"

    # node Mix Shader.002
    mix_shader_002 = martianrockshader.nodes.new("ShaderNodeMixShader")
    mix_shader_002.name = "Mix Shader.002"

    # node Mapping.001
    mapping_001_3 = martianrockshader.nodes.new("ShaderNodeMapping")
    mapping_001_3.name = "Mapping.001"
    mapping_001_3.vector_type = "POINT"
    # Rotation
    mapping_001_3.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    mapping_001_3.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Texture Coordinate.001
    texture_coordinate_001_1 = martianrockshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001_1.name = "Texture Coordinate.001"
    texture_coordinate_001_1.from_instancer = False
    texture_coordinate_001_1.outputs[0].hide = True
    texture_coordinate_001_1.outputs[1].hide = True
    texture_coordinate_001_1.outputs[2].hide = True
    texture_coordinate_001_1.outputs[4].hide = True
    texture_coordinate_001_1.outputs[5].hide = True
    texture_coordinate_001_1.outputs[6].hide = True

    # node Noise Texture.003
    noise_texture_003_2 = martianrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003_2.name = "Noise Texture.003"
    noise_texture_003_2.noise_dimensions = "3D"
    noise_texture_003_2.noise_type = "HETERO_TERRAIN"
    noise_texture_003_2.normalize = True
    # Detail
    noise_texture_003_2.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_003_2.inputs[4].default_value = 0.5166667103767395
    # Lacunarity
    noise_texture_003_2.inputs[5].default_value = 15.179998397827148
    # Offset
    noise_texture_003_2.inputs[6].default_value = 0.14000000059604645
    # Distortion
    noise_texture_003_2.inputs[8].default_value = 0.0

    # node Color Ramp.004
    color_ramp_004_2 = martianrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004_2.name = "Color Ramp.004"
    color_ramp_004_2.color_ramp.color_mode = "RGB"
    color_ramp_004_2.color_ramp.hue_interpolation = "NEAR"
    color_ramp_004_2.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp_004_2.color_ramp.elements.remove(color_ramp_004_2.color_ramp.elements[0])
    color_ramp_004_2_cre_0 = color_ramp_004_2.color_ramp.elements[0]
    color_ramp_004_2_cre_0.position = 0.18636341392993927
    color_ramp_004_2_cre_0.alpha = 1.0
    color_ramp_004_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_004_2_cre_1 = color_ramp_004_2.color_ramp.elements.new(
        0.9186362028121948
    )
    color_ramp_004_2_cre_1.alpha = 1.0
    color_ramp_004_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Map Range.002
    map_range_002 = martianrockshader.nodes.new("ShaderNodeMapRange")
    map_range_002.name = "Map Range.002"
    map_range_002.clamp = True
    map_range_002.data_type = "FLOAT"
    map_range_002.interpolation_type = "LINEAR"
    # From Min
    map_range_002.inputs[1].default_value = 0.0
    # From Max
    map_range_002.inputs[2].default_value = 1.0
    # To Min
    map_range_002.inputs[3].default_value = 0.020000003278255463
    # To Max
    map_range_002.inputs[4].default_value = 0.08000001311302185

    # node Noise Texture.005
    noise_texture_005_1 = martianrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_005_1.name = "Noise Texture.005"
    noise_texture_005_1.noise_dimensions = "3D"
    noise_texture_005_1.noise_type = "FBM"
    noise_texture_005_1.normalize = True
    # Detail
    noise_texture_005_1.inputs[3].default_value = 5.0
    # Roughness
    noise_texture_005_1.inputs[4].default_value = 0.6670835614204407
    # Lacunarity
    noise_texture_005_1.inputs[5].default_value = 5.0
    # Distortion
    noise_texture_005_1.inputs[8].default_value = 0.0

    # node Color Ramp.006
    color_ramp_006_2 = martianrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006_2.name = "Color Ramp.006"
    color_ramp_006_2.color_ramp.color_mode = "RGB"
    color_ramp_006_2.color_ramp.hue_interpolation = "NEAR"
    color_ramp_006_2.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp_006_2.color_ramp.elements.remove(color_ramp_006_2.color_ramp.elements[0])
    color_ramp_006_2_cre_0 = color_ramp_006_2.color_ramp.elements[0]
    color_ramp_006_2_cre_0.position = 0.5681818127632141
    color_ramp_006_2_cre_0.alpha = 1.0
    color_ramp_006_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_006_2_cre_1 = color_ramp_006_2.color_ramp.elements.new(
        0.7000001072883606
    )
    color_ramp_006_2_cre_1.alpha = 1.0
    color_ramp_006_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Map Range.007
    map_range_007 = martianrockshader.nodes.new("ShaderNodeMapRange")
    map_range_007.name = "Map Range.007"
    map_range_007.clamp = True
    map_range_007.data_type = "FLOAT"
    map_range_007.interpolation_type = "LINEAR"
    # From Min
    map_range_007.inputs[1].default_value = 0.0
    # From Max
    map_range_007.inputs[2].default_value = 1.0
    # To Min
    map_range_007.inputs[3].default_value = 0.02500000037252903
    # To Max
    map_range_007.inputs[4].default_value = 0.07500000298023224

    # node Map Range.015
    map_range_015 = martianrockshader.nodes.new("ShaderNodeMapRange")
    map_range_015.name = "Map Range.015"
    map_range_015.clamp = True
    map_range_015.data_type = "FLOAT"
    map_range_015.interpolation_type = "LINEAR"
    # From Min
    map_range_015.inputs[1].default_value = 0.0
    # From Max
    map_range_015.inputs[2].default_value = 1.0
    # To Min
    map_range_015.inputs[3].default_value = -1000.0
    # To Max
    map_range_015.inputs[4].default_value = 1000.0

    # node Group
    group = martianrockshader.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = random_x4___mat
    # Socket_5
    group.inputs[0].default_value = 0.521340012550354

    # node Combine Color.003
    combine_color_003 = martianrockshader.nodes.new("ShaderNodeCombineColor")
    combine_color_003.name = "Combine Color.003"
    combine_color_003.mode = "HSV"
    # Red
    combine_color_003.inputs[0].default_value = 0.033332519233226776
    # Green
    combine_color_003.inputs[1].default_value = 0.8999999761581421

    # node Map Range.008
    map_range_008 = martianrockshader.nodes.new("ShaderNodeMapRange")
    map_range_008.name = "Map Range.008"
    map_range_008.clamp = True
    map_range_008.data_type = "FLOAT"
    map_range_008.interpolation_type = "LINEAR"
    # Value
    map_range_008.inputs[0].default_value = 1.0
    # From Min
    map_range_008.inputs[1].default_value = 0.0
    # From Max
    map_range_008.inputs[2].default_value = 1.0
    # To Min
    map_range_008.inputs[3].default_value = 0.2900000214576721
    # To Max
    map_range_008.inputs[4].default_value = 0.7899999618530273

    # node Combine Color.006
    combine_color_006 = martianrockshader.nodes.new("ShaderNodeCombineColor")
    combine_color_006.name = "Combine Color.006"
    combine_color_006.mode = "HSV"
    # Red
    combine_color_006.inputs[0].default_value = 0.03500000014901161
    # Green
    combine_color_006.inputs[1].default_value = 0.08500000089406967

    # node Map Range.011
    map_range_011_2 = martianrockshader.nodes.new("ShaderNodeMapRange")
    map_range_011_2.name = "Map Range.011"
    map_range_011_2.clamp = True
    map_range_011_2.data_type = "FLOAT"
    map_range_011_2.interpolation_type = "LINEAR"
    # From Min
    map_range_011_2.inputs[1].default_value = 0.0
    # From Max
    map_range_011_2.inputs[2].default_value = 1.0
    # To Min
    map_range_011_2.inputs[3].default_value = 0.0
    # To Max
    map_range_011_2.inputs[4].default_value = 0.029999999329447746

    # Set locations
    group_output_7.location = (1658.8565673828125, -863.8759765625)
    group_005.location = (763.2269287109375, -820.1624755859375)
    group_006.location = (734.3885498046875, -1368.90478515625)
    combine_color_001.location = (163.7159423828125, -380.75921630859375)
    map_range_005.location = (-26.2840576171875, -331.75921630859375)
    combine_color_002.location = (163.7159423828125, -743.6762084960938)
    map_range_006.location = (-26.2840576171875, -694.6762084960938)
    group_008.location = (694.5396118164062, -193.486328125)
    mix_shader_001.location = (1074.927001953125, -875.521240234375)
    mix_shader_002.location = (1273.0546875, -662.526611328125)
    mapping_001_3.location = (-378.397705078125, 1248.543212890625)
    texture_coordinate_001_1.location = (-633.934814453125, 1283.7763671875)
    noise_texture_003_2.location = (69.0587158203125, 770.0805053710938)
    color_ramp_004_2.location = (272.8131103515625, 795.0889282226562)
    map_range_002.location = (-183.6375732421875, 819.4551391601562)
    noise_texture_005_1.location = (69.0587158203125, 259.23516845703125)
    color_ramp_006_2.location = (278.5709228515625, 285.52447509765625)
    map_range_007.location = (-183.6375732421875, 308.60980224609375)
    map_range_015.location = (-601.584228515625, 1054.19091796875)
    group.location = (-1002.6082763671875, -191.56527709960938)
    combine_color_003.location = (-471.6387939453125, -544.2174682617188)
    map_range_008.location = (-686.9805908203125, -567.8173828125)
    combine_color_006.location = (185.722900390625, -1101.7760009765625)
    map_range_011_2.location = (-31.125974655151367, -1067.997802734375)

    # initialize martianrockshader links
    # combine_color_002.Color -> group_006.Color 2
    martianrockshader.links.new(combine_color_002.outputs[0], group_006.inputs[2])
    # group.0 -> map_range_015.Value
    martianrockshader.links.new(group.outputs[0], map_range_015.inputs[0])
    # group.2 -> map_range_002.Value
    martianrockshader.links.new(group.outputs[2], map_range_002.inputs[0])
    # combine_color_001.Color -> group_005.Color 1
    martianrockshader.links.new(combine_color_001.outputs[0], group_005.inputs[1])
    # group_006.Shader -> mix_shader_001.Shader
    martianrockshader.links.new(group_006.outputs[0], mix_shader_001.inputs[2])
    # group.2 -> map_range_007.Value
    martianrockshader.links.new(group.outputs[2], map_range_007.inputs[0])
    # group_005.Shader -> mix_shader_001.Shader
    martianrockshader.links.new(group_005.outputs[0], mix_shader_001.inputs[1])
    # color_ramp_004_2.Color -> mix_shader_001.Fac
    martianrockshader.links.new(color_ramp_004_2.outputs[0], mix_shader_001.inputs[0])
    # mix_shader_001.Shader -> mix_shader_002.Shader
    martianrockshader.links.new(mix_shader_001.outputs[0], mix_shader_002.inputs[2])
    # color_ramp_006_2.Color -> mix_shader_002.Fac
    martianrockshader.links.new(color_ramp_006_2.outputs[0], mix_shader_002.inputs[0])
    # texture_coordinate_001_1.Object -> mapping_001_3.Vector
    martianrockshader.links.new(
        texture_coordinate_001_1.outputs[3], mapping_001_3.inputs[0]
    )
    # map_range_005.Result -> combine_color_001.Blue
    martianrockshader.links.new(map_range_005.outputs[0], combine_color_001.inputs[2])
    # combine_color_001.Color -> group_008.Edge Lightness
    martianrockshader.links.new(combine_color_001.outputs[0], group_008.inputs[3])
    # map_range_006.Result -> combine_color_002.Blue
    martianrockshader.links.new(map_range_006.outputs[0], combine_color_002.inputs[2])
    # combine_color_002.Color -> group_008.Rock Color 1
    martianrockshader.links.new(combine_color_002.outputs[0], group_008.inputs[1])
    # noise_texture_003_2.Fac -> color_ramp_004_2.Fac
    martianrockshader.links.new(
        noise_texture_003_2.outputs[0], color_ramp_004_2.inputs[0]
    )
    # mapping_001_3.Vector -> noise_texture_003_2.Vector
    martianrockshader.links.new(mapping_001_3.outputs[0], noise_texture_003_2.inputs[0])
    # map_range_002.Result -> noise_texture_003_2.Scale
    martianrockshader.links.new(map_range_002.outputs[0], noise_texture_003_2.inputs[2])
    # group.1 -> map_range_005.Value
    martianrockshader.links.new(group.outputs[1], map_range_005.inputs[0])
    # map_range_015.Result -> mapping_001_3.Location
    martianrockshader.links.new(map_range_015.outputs[0], mapping_001_3.inputs[1])
    # noise_texture_005_1.Fac -> color_ramp_006_2.Fac
    martianrockshader.links.new(
        noise_texture_005_1.outputs[0], color_ramp_006_2.inputs[0]
    )
    # combine_color_002.Color -> group_005.Color 4
    martianrockshader.links.new(combine_color_002.outputs[0], group_005.inputs[4])
    # mapping_001_3.Vector -> noise_texture_005_1.Vector
    martianrockshader.links.new(mapping_001_3.outputs[0], noise_texture_005_1.inputs[0])
    # map_range_007.Result -> noise_texture_005_1.Scale
    martianrockshader.links.new(map_range_007.outputs[0], noise_texture_005_1.inputs[2])
    # combine_color_001.Color -> group_006.Color 3
    martianrockshader.links.new(combine_color_001.outputs[0], group_006.inputs[3])
    # mix_shader_002.Shader -> group_output_7.Shader
    martianrockshader.links.new(mix_shader_002.outputs[0], group_output_7.inputs[0])
    # group_008.BSDF -> mix_shader_002.Shader
    martianrockshader.links.new(group_008.outputs[0], mix_shader_002.inputs[1])
    # group.0 -> map_range_006.Value
    martianrockshader.links.new(group.outputs[0], map_range_006.inputs[0])
    # group.3 -> group_008.Noise scale mixer
    martianrockshader.links.new(group.outputs[3], group_008.inputs[14])
    # combine_color_006.Color -> group_008.Rock Color 2
    martianrockshader.links.new(combine_color_006.outputs[0], group_008.inputs[2])
    # combine_color_006.Color -> group_005.Color 2
    martianrockshader.links.new(combine_color_006.outputs[0], group_005.inputs[2])
    # combine_color_006.Color -> group_006.Color 1
    martianrockshader.links.new(combine_color_006.outputs[0], group_006.inputs[1])
    # combine_color_006.Color -> group_005.Color 3
    martianrockshader.links.new(combine_color_006.outputs[0], group_005.inputs[3])
    # map_range_008.Result -> combine_color_003.Blue
    martianrockshader.links.new(map_range_008.outputs[0], combine_color_003.inputs[2])
    # map_range_011_2.Result -> combine_color_006.Blue
    martianrockshader.links.new(map_range_011_2.outputs[0], combine_color_006.inputs[2])
    # group.4 -> map_range_011_2.Value
    martianrockshader.links.new(group.outputs[4], map_range_011_2.inputs[0])
    return martianrockshader


martianrockshader = martianrockshader_node_group()


# initialize MartianSurface node group
def martiansurface_node_group():
    martiansurface = mat.node_tree
    # start with a clean node tree
    for node in martiansurface.nodes:
        martiansurface.nodes.remove(node)
    martiansurface.color_tag = "NONE"
    martiansurface.description = ""
    martiansurface.default_group_node_width = 140

    # martiansurface interface

    # initialize martiansurface nodes
    # node Material Output
    material_output = martiansurface.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = "ALL"
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0

    # node Geometry
    geometry_1 = martiansurface.nodes.new("ShaderNodeNewGeometry")
    geometry_1.name = "Geometry"

    # node Color Ramp
    color_ramp_2 = martiansurface.nodes.new("ShaderNodeValToRGB")
    color_ramp_2.name = "Color Ramp"
    color_ramp_2.color_ramp.color_mode = "RGB"
    color_ramp_2.color_ramp.hue_interpolation = "NEAR"
    color_ramp_2.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp_2.color_ramp.elements.remove(color_ramp_2.color_ramp.elements[0])
    color_ramp_2_cre_0 = color_ramp_2.color_ramp.elements[0]
    color_ramp_2_cre_0.position = 0.7045449018478394
    color_ramp_2_cre_0.alpha = 1.0
    color_ramp_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_2_cre_1 = color_ramp_2.color_ramp.elements.new(0.8000001907348633)
    color_ramp_2_cre_1.alpha = 1.0
    color_ramp_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Mapping.001
    mapping_001_4 = martiansurface.nodes.new("ShaderNodeMapping")
    mapping_001_4.name = "Mapping.001"
    mapping_001_4.vector_type = "POINT"
    # Rotation
    mapping_001_4.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    mapping_001_4.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Texture Coordinate.001
    texture_coordinate_001_2 = martiansurface.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001_2.name = "Texture Coordinate.001"
    texture_coordinate_001_2.from_instancer = False
    texture_coordinate_001_2.outputs[0].hide = True
    texture_coordinate_001_2.outputs[1].hide = True
    texture_coordinate_001_2.outputs[2].hide = True
    texture_coordinate_001_2.outputs[4].hide = True
    texture_coordinate_001_2.outputs[5].hide = True
    texture_coordinate_001_2.outputs[6].hide = True

    # node Math
    math_4 = martiansurface.nodes.new("ShaderNodeMath")
    math_4.name = "Math"
    math_4.operation = "ADD"
    math_4.use_clamp = False

    # node Separate XYZ
    separate_xyz = martiansurface.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[2].hide = True

    # node Mix
    mix_4 = martiansurface.nodes.new("ShaderNodeMix")
    mix_4.name = "Mix"
    mix_4.blend_type = "MIX"
    mix_4.clamp_factor = True
    mix_4.clamp_result = False
    mix_4.data_type = "FLOAT"
    mix_4.factor_mode = "UNIFORM"
    mix_4.inputs[0].hide = True
    mix_4.inputs[1].hide = True
    mix_4.inputs[4].hide = True
    mix_4.inputs[5].hide = True
    mix_4.inputs[6].hide = True
    mix_4.inputs[7].hide = True
    mix_4.inputs[8].hide = True
    mix_4.inputs[9].hide = True
    mix_4.outputs[1].hide = True
    mix_4.outputs[2].hide = True
    mix_4.outputs[3].hide = True
    # Factor_Float
    mix_4.inputs[0].default_value = 0.5

    # node Vector Math
    vector_math = martiansurface.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = "ABSOLUTE"

    # node Math.001
    math_001_2 = martiansurface.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.operation = "MULTIPLY"
    math_001_2.use_clamp = False
    # Value_001
    math_001_2.inputs[1].default_value = 0.550000011920929

    # node Group.002
    group_002_1 = martiansurface.nodes.new("ShaderNodeGroup")
    group_002_1.name = "Group.002"
    group_002_1.node_tree = rockygroundshader
    # Socket_2
    group_002_1.inputs[0].default_value = 0.10000000149011612
    # Socket_4
    group_002_1.inputs[1].default_value = 1.0
    # Socket_7
    group_002_1.inputs[4].default_value = 0.3499999940395355
    # Socket_8
    group_002_1.inputs[5].default_value = 25.0
    # Socket_9
    group_002_1.inputs[6].default_value = 100.0
    # Socket_13
    group_002_1.inputs[10].default_value = 1.5
    # Socket_14
    group_002_1.inputs[11].default_value = 0.15000000596046448
    # Socket_15
    group_002_1.inputs[12].default_value = 0.699999988079071
    # Socket_16
    group_002_1.inputs[13].default_value = 0.20000000298023224

    # node Mix Shader.001
    mix_shader_001_1 = martiansurface.nodes.new("ShaderNodeMixShader")
    mix_shader_001_1.name = "Mix Shader.001"

    # node Noise Texture.003
    noise_texture_003_3 = martiansurface.nodes.new("ShaderNodeTexNoise")
    noise_texture_003_3.name = "Noise Texture.003"
    noise_texture_003_3.noise_dimensions = "3D"
    noise_texture_003_3.noise_type = "HETERO_TERRAIN"
    noise_texture_003_3.normalize = True
    # Detail
    noise_texture_003_3.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_003_3.inputs[4].default_value = 0.6516672968864441
    # Lacunarity
    noise_texture_003_3.inputs[5].default_value = 2.059999465942383
    # Offset
    noise_texture_003_3.inputs[6].default_value = 0.0
    # Distortion
    noise_texture_003_3.inputs[8].default_value = 0.0

    # node Color Ramp.004
    color_ramp_004_3 = martiansurface.nodes.new("ShaderNodeValToRGB")
    color_ramp_004_3.name = "Color Ramp.004"
    color_ramp_004_3.color_ramp.color_mode = "RGB"
    color_ramp_004_3.color_ramp.hue_interpolation = "NEAR"
    color_ramp_004_3.color_ramp.interpolation = "B_SPLINE"

    # initialize color ramp elements
    color_ramp_004_3.color_ramp.elements.remove(color_ramp_004_3.color_ramp.elements[0])
    color_ramp_004_3_cre_0 = color_ramp_004_3.color_ramp.elements[0]
    color_ramp_004_3_cre_0.position = 0.149999737739563
    color_ramp_004_3_cre_0.alpha = 1.0
    color_ramp_004_3_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_004_3_cre_1 = color_ramp_004_3.color_ramp.elements.new(1.0)
    color_ramp_004_3_cre_1.alpha = 1.0
    color_ramp_004_3_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Map Range.002
    map_range_002_1 = martiansurface.nodes.new("ShaderNodeMapRange")
    map_range_002_1.name = "Map Range.002"
    map_range_002_1.clamp = True
    map_range_002_1.data_type = "FLOAT"
    map_range_002_1.interpolation_type = "LINEAR"
    # From Min
    map_range_002_1.inputs[1].default_value = 0.0
    # From Max
    map_range_002_1.inputs[2].default_value = 1.0
    # To Min
    map_range_002_1.inputs[3].default_value = 0.05000000074505806
    # To Max
    map_range_002_1.inputs[4].default_value = 0.07500000298023224

    # node Group.004
    group_004 = martiansurface.nodes.new("ShaderNodeGroup")
    group_004.name = "Group.004"
    group_004.node_tree = sandshader
    # Socket_1
    group_004.inputs[0].default_value = 20.0
    # Socket_2
    group_004.inputs[1].default_value = 135.0
    # Socket_3
    group_004.inputs[2].default_value = 5.0
    # Socket_7
    group_004.inputs[6].default_value = 15.0
    # Socket_8
    group_004.inputs[7].default_value = 1.0
    # Socket_9
    group_004.inputs[8].default_value = 0.019999999552965164
    # Socket_10
    group_004.inputs[9].default_value = 0.10000000149011612
    # Socket_11
    group_004.inputs[10].default_value = 0.10000000149011612

    # node Noise Texture.005
    noise_texture_005_2 = martiansurface.nodes.new("ShaderNodeTexNoise")
    noise_texture_005_2.name = "Noise Texture.005"
    noise_texture_005_2.noise_dimensions = "3D"
    noise_texture_005_2.noise_type = "FBM"
    noise_texture_005_2.normalize = True
    # Detail
    noise_texture_005_2.inputs[3].default_value = 5.0
    # Roughness
    noise_texture_005_2.inputs[4].default_value = 0.6670835614204407
    # Lacunarity
    noise_texture_005_2.inputs[5].default_value = 5.0
    # Distortion
    noise_texture_005_2.inputs[8].default_value = 0.0

    # node Color Ramp.006
    color_ramp_006_3 = martiansurface.nodes.new("ShaderNodeValToRGB")
    color_ramp_006_3.name = "Color Ramp.006"
    color_ramp_006_3.color_ramp.color_mode = "RGB"
    color_ramp_006_3.color_ramp.hue_interpolation = "NEAR"
    color_ramp_006_3.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp_006_3.color_ramp.elements.remove(color_ramp_006_3.color_ramp.elements[0])
    color_ramp_006_3_cre_0 = color_ramp_006_3.color_ramp.elements[0]
    color_ramp_006_3_cre_0.position = 0.454545795917511
    color_ramp_006_3_cre_0.alpha = 1.0
    color_ramp_006_3_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_006_3_cre_1 = color_ramp_006_3.color_ramp.elements.new(
        0.7227275371551514
    )
    color_ramp_006_3_cre_1.alpha = 1.0
    color_ramp_006_3_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Map Range.007
    map_range_007_1 = martiansurface.nodes.new("ShaderNodeMapRange")
    map_range_007_1.name = "Map Range.007"
    map_range_007_1.clamp = True
    map_range_007_1.data_type = "FLOAT"
    map_range_007_1.interpolation_type = "LINEAR"
    # From Min
    map_range_007_1.inputs[1].default_value = 0.0
    # From Max
    map_range_007_1.inputs[2].default_value = 1.0
    # To Min
    map_range_007_1.inputs[3].default_value = 0.02500000037252903
    # To Max
    map_range_007_1.inputs[4].default_value = 0.07500000298023224

    # node Mix Shader.003
    mix_shader_003 = martiansurface.nodes.new("ShaderNodeMixShader")
    mix_shader_003.name = "Mix Shader.003"

    # node Map Range.011
    map_range_011_3 = martiansurface.nodes.new("ShaderNodeMapRange")
    map_range_011_3.name = "Map Range.011"
    map_range_011_3.clamp = True
    map_range_011_3.data_type = "FLOAT"
    map_range_011_3.interpolation_type = "LINEAR"
    # From Min
    map_range_011_3.inputs[1].default_value = 0.0
    # From Max
    map_range_011_3.inputs[2].default_value = 1.0
    # To Min
    map_range_011_3.inputs[3].default_value = -1000.0
    # To Max
    map_range_011_3.inputs[4].default_value = 1000.0

    # node Combine Color.001
    combine_color_001_1 = martiansurface.nodes.new("ShaderNodeCombineColor")
    combine_color_001_1.name = "Combine Color.001"
    combine_color_001_1.mode = "HSV"
    # Red
    combine_color_001_1.inputs[0].default_value = 0.033332519233226776
    # Green
    combine_color_001_1.inputs[1].default_value = 0.8999999761581421

    # node Map Range.005
    map_range_005_1 = martiansurface.nodes.new("ShaderNodeMapRange")
    map_range_005_1.name = "Map Range.005"
    map_range_005_1.clamp = True
    map_range_005_1.data_type = "FLOAT"
    map_range_005_1.interpolation_type = "LINEAR"
    # From Min
    map_range_005_1.inputs[1].default_value = 0.0
    # From Max
    map_range_005_1.inputs[2].default_value = 1.0
    # To Min
    map_range_005_1.inputs[3].default_value = 0.2900000214576721
    # To Max
    map_range_005_1.inputs[4].default_value = 0.7899999618530273

    # node Combine Color.002
    combine_color_002_1 = martiansurface.nodes.new("ShaderNodeCombineColor")
    combine_color_002_1.name = "Combine Color.002"
    combine_color_002_1.mode = "HSV"
    # Red
    combine_color_002_1.inputs[0].default_value = 0.021490026265382767
    # Green
    combine_color_002_1.inputs[1].default_value = 0.8500000238418579

    # node Map Range.006
    map_range_006_1 = martiansurface.nodes.new("ShaderNodeMapRange")
    map_range_006_1.name = "Map Range.006"
    map_range_006_1.clamp = True
    map_range_006_1.data_type = "FLOAT"
    map_range_006_1.interpolation_type = "LINEAR"
    # From Min
    map_range_006_1.inputs[1].default_value = 0.0
    # From Max
    map_range_006_1.inputs[2].default_value = 1.0
    # To Min
    map_range_006_1.inputs[3].default_value = 0.009999999776482582
    # To Max
    map_range_006_1.inputs[4].default_value = 0.019999999552965164

    # node Combine Color.004
    combine_color_004 = martiansurface.nodes.new("ShaderNodeCombineColor")
    combine_color_004.name = "Combine Color.004"
    combine_color_004.mode = "HSV"
    # Red
    combine_color_004.inputs[0].default_value = 0.03500000014901161
    # Green
    combine_color_004.inputs[1].default_value = 0.08500000089406967

    # node Group
    group_1 = martiansurface.nodes.new("ShaderNodeGroup")
    group_1.name = "Group"
    group_1.node_tree = martianrockshader

    # node Combine Color.003
    combine_color_003_1 = martiansurface.nodes.new("ShaderNodeCombineColor")
    combine_color_003_1.name = "Combine Color.003"
    combine_color_003_1.mode = "HSV"
    # Red
    combine_color_003_1.inputs[0].default_value = 0.05000000074505806

    # node Map Range.008
    map_range_008_1 = martiansurface.nodes.new("ShaderNodeMapRange")
    map_range_008_1.name = "Map Range.008"
    map_range_008_1.clamp = True
    map_range_008_1.data_type = "FLOAT"
    map_range_008_1.interpolation_type = "LINEAR"
    # From Min
    map_range_008_1.inputs[1].default_value = 0.0
    # From Max
    map_range_008_1.inputs[2].default_value = 1.0
    # To Min
    map_range_008_1.inputs[3].default_value = 0.4000000059604645
    # To Max
    map_range_008_1.inputs[4].default_value = 0.699999988079071

    # node Map Range.013
    map_range_013 = martiansurface.nodes.new("ShaderNodeMapRange")
    map_range_013.name = "Map Range.013"
    map_range_013.clamp = True
    map_range_013.data_type = "FLOAT"
    map_range_013.interpolation_type = "LINEAR"
    # From Min
    map_range_013.inputs[1].default_value = 0.0
    # From Max
    map_range_013.inputs[2].default_value = 1.0
    # To Min
    map_range_013.inputs[3].default_value = 0.6000000238418579
    # To Max
    map_range_013.inputs[4].default_value = 0.800000011920929

    # node Group.001
    group_001_5 = martiansurface.nodes.new("ShaderNodeGroup")
    group_001_5.name = "Group.001"
    group_001_5.node_tree = random_x4___mat
    # Socket_5
    group_001_5.inputs[0].default_value = 0.8831431865692139

    # node Mix.002
    mix_002_3 = martiansurface.nodes.new("ShaderNodeMix")
    mix_002_3.name = "Mix.002"
    mix_002_3.blend_type = "SUBTRACT"
    mix_002_3.clamp_factor = False
    mix_002_3.clamp_result = True
    mix_002_3.data_type = "RGBA"
    mix_002_3.factor_mode = "UNIFORM"
    # Factor_Float
    mix_002_3.inputs[0].default_value = 1.0

    # node Mix.001
    mix_001_5 = martiansurface.nodes.new("ShaderNodeMix")
    mix_001_5.name = "Mix.001"
    mix_001_5.blend_type = "ADD"
    mix_001_5.clamp_factor = True
    mix_001_5.clamp_result = False
    mix_001_5.data_type = "RGBA"
    mix_001_5.factor_mode = "UNIFORM"
    # Factor_Float
    mix_001_5.inputs[0].default_value = 1.0

    # node Map Range.009
    map_range_009 = martiansurface.nodes.new("ShaderNodeMapRange")
    map_range_009.name = "Map Range.009"
    map_range_009.clamp = True
    map_range_009.data_type = "FLOAT"
    map_range_009.interpolation_type = "LINEAR"
    # From Min
    map_range_009.inputs[1].default_value = 0.0
    # From Max
    map_range_009.inputs[2].default_value = 1.0
    # To Min
    map_range_009.inputs[3].default_value = 0.0
    # To Max
    map_range_009.inputs[4].default_value = 0.029999999329447746

    # Set locations
    material_output.location = (206.30491638183594, 42.185760498046875)
    geometry_1.location = (-2425.501708984375, 2021.6300048828125)
    color_ramp_2.location = (-1253.8013916015625, 1975.7489013671875)
    mapping_001_4.location = (-2158.288330078125, 1531.86474609375)
    texture_coordinate_001_2.location = (-2508.998291015625, 1641.892822265625)
    math_4.location = (-1463.4637451171875, 1968.1905517578125)
    separate_xyz.location = (-2014.240478515625, 2113.76953125)
    mix_4.location = (-1825.476318359375, 2157.81103515625)
    vector_math.location = (-2179.816650390625, 2099.37646484375)
    math_001_2.location = (-1645.2833251953125, 2137.73388671875)
    group_002_1.location = (-1492.88427734375, 64.24871826171875)
    mix_shader_001_1.location = (-56.02490234375, 103.8680419921875)
    noise_texture_003_3.location = (-1663.0186767578125, 1332.224853515625)
    color_ramp_004_3.location = (-1422.188232421875, 1338.8973388671875)
    map_range_002_1.location = (-1915.7149658203125, 1381.599609375)
    group_004.location = (-1485.5966796875, -513.8714599609375)
    noise_texture_005_2.location = (-1648.9488525390625, 879.53515625)
    color_ramp_006_3.location = (-1424.117431640625, 894.8799438476562)
    map_range_007_1.location = (-1901.6451416015625, 928.909912109375)
    mix_shader_003.location = (-884.7830200195312, -125.24784851074219)
    map_range_011_3.location = (-2369.97021484375, 1501.8062744140625)
    combine_color_001_1.location = (-1848.130615234375, -9.55667495727539)
    map_range_005_1.location = (-2063.472412109375, -33.156612396240234)
    combine_color_002_1.location = (-1848.130615234375, -372.4736022949219)
    map_range_006_1.location = (-2048.09716796875, -311.56591796875)
    combine_color_004.location = (-1844.5869140625, -656.2456665039062)
    group_1.location = (-287.6199035644531, -105.33534240722656)
    combine_color_003_1.location = (-1848.130615234375, 303.6287536621094)
    map_range_008_1.location = (-2038.130615234375, 413.1502685546875)
    map_range_013.location = (-2294.1044921875, 308.190673828125)
    group_001_5.location = (-3285.98388671875, 824.70068359375)
    mix_002_3.location = (-886.1047973632812, 1298.42431640625)
    mix_001_5.location = (-849.9058837890625, 1648.1424560546875)
    map_range_009.location = (-2061.435791015625, -622.467529296875)

    # initialize martiansurface links
    # texture_coordinate_001_2.Object -> mapping_001_4.Vector
    martiansurface.links.new(
        texture_coordinate_001_2.outputs[3], mapping_001_4.inputs[0]
    )
    # vector_math.Vector -> separate_xyz.Vector
    martiansurface.links.new(vector_math.outputs[0], separate_xyz.inputs[0])
    # geometry_1.Pointiness -> math_4.Value
    martiansurface.links.new(geometry_1.outputs[7], math_4.inputs[1])
    # math_4.Value -> color_ramp_2.Fac
    martiansurface.links.new(math_4.outputs[0], color_ramp_2.inputs[0])
    # separate_xyz.X -> mix_4.A
    martiansurface.links.new(separate_xyz.outputs[0], mix_4.inputs[2])
    # separate_xyz.Y -> mix_4.B
    martiansurface.links.new(separate_xyz.outputs[1], mix_4.inputs[3])
    # math_001_2.Value -> math_4.Value
    martiansurface.links.new(math_001_2.outputs[0], math_4.inputs[0])
    # geometry_1.Normal -> vector_math.Vector
    martiansurface.links.new(geometry_1.outputs[1], vector_math.inputs[0])
    # mix_4.Result -> math_001_2.Value
    martiansurface.links.new(mix_4.outputs[0], math_001_2.inputs[0])
    # noise_texture_003_3.Fac -> color_ramp_004_3.Fac
    martiansurface.links.new(noise_texture_003_3.outputs[0], color_ramp_004_3.inputs[0])
    # mapping_001_4.Vector -> noise_texture_003_3.Vector
    martiansurface.links.new(mapping_001_4.outputs[0], noise_texture_003_3.inputs[0])
    # map_range_002_1.Result -> noise_texture_003_3.Scale
    martiansurface.links.new(map_range_002_1.outputs[0], noise_texture_003_3.inputs[2])
    # map_range_011_3.Result -> mapping_001_4.Location
    martiansurface.links.new(map_range_011_3.outputs[0], mapping_001_4.inputs[1])
    # group_001_5.1 -> map_range_002_1.Value
    martiansurface.links.new(group_001_5.outputs[1], map_range_002_1.inputs[0])
    # noise_texture_005_2.Fac -> color_ramp_006_3.Fac
    martiansurface.links.new(noise_texture_005_2.outputs[0], color_ramp_006_3.inputs[0])
    # mapping_001_4.Vector -> noise_texture_005_2.Vector
    martiansurface.links.new(mapping_001_4.outputs[0], noise_texture_005_2.inputs[0])
    # group_001_5.2 -> map_range_007_1.Value
    martiansurface.links.new(group_001_5.outputs[2], map_range_007_1.inputs[0])
    # map_range_007_1.Result -> noise_texture_005_2.Scale
    martiansurface.links.new(map_range_007_1.outputs[0], noise_texture_005_2.inputs[2])
    # group_001_5.0 -> map_range_011_3.Value
    martiansurface.links.new(group_001_5.outputs[0], map_range_011_3.inputs[0])
    # map_range_005_1.Result -> combine_color_001_1.Blue
    martiansurface.links.new(map_range_005_1.outputs[0], combine_color_001_1.inputs[2])
    # map_range_006_1.Result -> combine_color_002_1.Blue
    martiansurface.links.new(map_range_006_1.outputs[0], combine_color_002_1.inputs[2])
    # group_001_5.0 -> map_range_005_1.Value
    martiansurface.links.new(group_001_5.outputs[0], map_range_005_1.inputs[0])
    # group_001_5.3 -> map_range_006_1.Value
    martiansurface.links.new(group_001_5.outputs[3], map_range_006_1.inputs[0])
    # map_range_008_1.Result -> combine_color_003_1.Blue
    martiansurface.links.new(map_range_008_1.outputs[0], combine_color_003_1.inputs[2])
    # map_range_013.Result -> combine_color_003_1.Green
    martiansurface.links.new(map_range_013.outputs[0], combine_color_003_1.inputs[1])
    # group_001_5.4 -> map_range_013.Value
    martiansurface.links.new(group_001_5.outputs[4], map_range_013.inputs[0])
    # group_001_5.3 -> map_range_008_1.Value
    martiansurface.links.new(group_001_5.outputs[3], map_range_008_1.inputs[0])
    # combine_color_003_1.Color -> group_002_1.Rock Color 1
    martiansurface.links.new(combine_color_003_1.outputs[0], group_002_1.inputs[2])
    # combine_color_002_1.Color -> group_002_1.Dirt Color 2
    martiansurface.links.new(combine_color_002_1.outputs[0], group_002_1.inputs[8])
    # combine_color_001_1.Color -> group_002_1.Dirt Color 1
    martiansurface.links.new(combine_color_001_1.outputs[0], group_002_1.inputs[7])
    # combine_color_004.Color -> group_002_1.Dirt Color 3
    martiansurface.links.new(combine_color_004.outputs[0], group_002_1.inputs[9])
    # combine_color_001_1.Color -> group_004.Sand Color 1
    martiansurface.links.new(combine_color_001_1.outputs[0], group_004.inputs[4])
    # group_1.Shader -> mix_shader_001_1.Shader
    martiansurface.links.new(group_1.outputs[0], mix_shader_001_1.inputs[2])
    # mix_001_5.Result -> mix_shader_001_1.Fac
    martiansurface.links.new(mix_001_5.outputs[2], mix_shader_001_1.inputs[0])
    # group_002_1.Shader -> mix_shader_003.Shader
    martiansurface.links.new(group_002_1.outputs[0], mix_shader_003.inputs[2])
    # group_004.BSDF -> mix_shader_003.Shader
    martiansurface.links.new(group_004.outputs[0], mix_shader_003.inputs[1])
    # mix_shader_003.Shader -> mix_shader_001_1.Shader
    martiansurface.links.new(mix_shader_003.outputs[0], mix_shader_001_1.inputs[1])
    # color_ramp_004_3.Color -> mix_002_3.A
    martiansurface.links.new(color_ramp_004_3.outputs[0], mix_002_3.inputs[6])
    # color_ramp_2.Color -> mix_002_3.B
    martiansurface.links.new(color_ramp_2.outputs[0], mix_002_3.inputs[7])
    # mix_002_3.Result -> mix_shader_003.Fac
    martiansurface.links.new(mix_002_3.outputs[2], mix_shader_003.inputs[0])
    # color_ramp_2.Color -> mix_001_5.A
    martiansurface.links.new(color_ramp_2.outputs[0], mix_001_5.inputs[6])
    # color_ramp_006_3.Color -> mix_001_5.B
    martiansurface.links.new(color_ramp_006_3.outputs[0], mix_001_5.inputs[7])
    # combine_color_001_1.Color -> group_002_1.Rock Color 2
    martiansurface.links.new(combine_color_001_1.outputs[0], group_002_1.inputs[3])
    # combine_color_002_1.Color -> group_004.Sand Color 2
    martiansurface.links.new(combine_color_002_1.outputs[0], group_004.inputs[5])
    # combine_color_004.Color -> group_004.Rock Color
    martiansurface.links.new(combine_color_004.outputs[0], group_004.inputs[3])
    # group_001_5.1 -> map_range_009.Value
    martiansurface.links.new(group_001_5.outputs[1], map_range_009.inputs[0])
    # map_range_009.Result -> combine_color_004.Blue
    martiansurface.links.new(map_range_009.outputs[0], combine_color_004.inputs[2])
    # mix_shader_001_1.Shader -> material_output.Surface
    martiansurface.links.new(mix_shader_001_1.outputs[0], material_output.inputs[0])
    return martiansurface


martiansurface = martiansurface_node_group()
