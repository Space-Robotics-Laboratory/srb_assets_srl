import bpy

mat = bpy.data.materials.new(name="LunarRock")
mat.use_nodes = True


# initialize Random x4 | Mat node group
def random_x4___mat_node_group():
    random_x4___mat = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="Random x4 | Mat"
    )

    random_x4___mat.color_tag = "NONE"
    random_x4___mat.description = ""

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


# initialize RockShader node group
def rockshader_node_group():
    rockshader = bpy.data.node_groups.new(type="ShaderNodeTree", name="RockShader")

    rockshader.color_tag = "NONE"
    rockshader.description = ""

    # rockshader interface
    # Socket BSDF
    bsdf_socket = rockshader.interface.new_socket(
        name="BSDF", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    bsdf_socket.attribute_domain = "POINT"

    # Socket Scale
    scale_socket = rockshader.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    scale_socket.default_value = 1.0
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e38
    scale_socket.subtype = "NONE"
    scale_socket.attribute_domain = "POINT"

    # Socket Rock Color 1
    rock_color_1_socket = rockshader.interface.new_socket(
        name="Rock Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    rock_color_1_socket.default_value = (
        0.015996191650629044,
        0.015996308997273445,
        0.015996301546692848,
        1.0,
    )
    rock_color_1_socket.attribute_domain = "POINT"

    # Socket Rock Color 2
    rock_color_2_socket = rockshader.interface.new_socket(
        name="Rock Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    rock_color_2_socket.default_value = (0.0, 0.0, 0.0, 1.0)
    rock_color_2_socket.attribute_domain = "POINT"

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
    noise_scale_socket = rockshader.interface.new_socket(
        name="Noise Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    noise_scale_socket.default_value = 12.799999237060547
    noise_scale_socket.min_value = -1000.0
    noise_scale_socket.max_value = 1000.0
    noise_scale_socket.subtype = "NONE"
    noise_scale_socket.attribute_domain = "POINT"

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
    group_output_1 = rockshader.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # node Group Input
    group_input_1 = rockshader.nodes.new("NodeGroupInput")
    group_input_1.label = "Rock Color 2"
    group_input_1.name = "Group Input"

    # node Noise Texture
    noise_texture = rockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = "4D"
    noise_texture.noise_type = "FBM"
    noise_texture.normalize = True
    # Lacunarity
    noise_texture.inputs[5].default_value = 20.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # node Mapping.001
    mapping_001 = rockshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = "POINT"
    # Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)

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
    bump = rockshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    # Distance
    bump.inputs[1].default_value = 1.0

    # node Color Ramp
    color_ramp = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = "RGB"
    color_ramp.color_ramp.hue_interpolation = "NEAR"
    color_ramp.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.30181822180747986
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(0.3945455849170685)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Noise Texture.001
    noise_texture_001 = rockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = "4D"
    noise_texture_001.noise_type = "FBM"
    noise_texture_001.normalize = True
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    # node Color Ramp.001
    color_ramp_001 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.name = "Color Ramp.001"
    color_ramp_001.color_ramp.color_mode = "RGB"
    color_ramp_001.color_ramp.hue_interpolation = "NEAR"
    color_ramp_001.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
    color_ramp_001_cre_0.position = 0.4054546356201172
    color_ramp_001_cre_0.alpha = 1.0
    color_ramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.64090895652771)
    color_ramp_001_cre_1.alpha = 1.0
    color_ramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Mix
    mix = rockshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = "MIX"
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = "RGBA"
    mix.factor_mode = "UNIFORM"

    # node Mix.001
    mix_001 = rockshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = "MIX"
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = "RGBA"
    mix_001.factor_mode = "UNIFORM"

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
    color_ramp_002 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_002.name = "Color Ramp.002"
    color_ramp_002.color_ramp.color_mode = "RGB"
    color_ramp_002.color_ramp.hue_interpolation = "NEAR"
    color_ramp_002.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp_002.color_ramp.elements.remove(color_ramp_002.color_ramp.elements[0])
    color_ramp_002_cre_0 = color_ramp_002.color_ramp.elements[0]
    color_ramp_002_cre_0.position = 0.5186362266540527
    color_ramp_002_cre_0.alpha = 1.0
    color_ramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_002_cre_1 = color_ramp_002.color_ramp.elements.new(0.6045457124710083)
    color_ramp_002_cre_1.alpha = 1.0
    color_ramp_002_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Mix.003
    mix_003 = rockshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = "MIX"
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = "RGBA"
    mix_003.factor_mode = "UNIFORM"

    # node Color Ramp.004
    color_ramp_004 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = "RGB"
    color_ramp_004.color_ramp.hue_interpolation = "NEAR"
    color_ramp_004.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.0
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (
        0.6514015197753906,
        0.6514063477516174,
        0.6514060497283936,
        1.0,
    )

    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(1.0)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Noise Texture.003
    noise_texture_003 = rockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003.name = "Noise Texture.003"
    noise_texture_003.noise_dimensions = "4D"
    noise_texture_003.noise_type = "FBM"
    noise_texture_003.normalize = True
    # Detail
    noise_texture_003.inputs[3].default_value = 15.0
    # Lacunarity
    noise_texture_003.inputs[5].default_value = 0.0
    # Distortion
    noise_texture_003.inputs[8].default_value = 0.0

    # node Bump.001
    bump_001 = rockshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    # Distance
    bump_001.inputs[1].default_value = 1.0

    # node Frame.001
    frame_001 = rockshader.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # node Frame.002
    frame_002 = rockshader.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # node Frame
    frame = rockshader.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # node Hue/Saturation/Value
    hue_saturation_value = rockshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    # Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    # node Frame.003
    frame_003 = rockshader.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # node Principled BSDF
    principled_bsdf = rockshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = "MULTI_GGX"
    principled_bsdf.subsurface_method = "RANDOM_WALK"
    # Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    # IOR
    principled_bsdf.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    # Subsurface Weight
    principled_bsdf.inputs[7].default_value = 0.0
    # Subsurface Radius
    principled_bsdf.inputs[8].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf.inputs[9].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf.inputs[11].default_value = 0.0
    # Specular IOR Level
    principled_bsdf.inputs[12].default_value = 0.5
    # Specular Tint
    principled_bsdf.inputs[13].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf.inputs[14].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf.inputs[15].default_value = 0.0
    # Tangent
    principled_bsdf.inputs[16].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf.inputs[17].default_value = 0.0
    # Coat Weight
    principled_bsdf.inputs[18].default_value = 0.0
    # Coat Roughness
    principled_bsdf.inputs[19].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf.inputs[20].default_value = 1.5
    # Coat Tint
    principled_bsdf.inputs[21].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf.inputs[22].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf.inputs[23].default_value = 0.0
    # Sheen Roughness
    principled_bsdf.inputs[24].default_value = 0.5
    # Sheen Tint
    principled_bsdf.inputs[25].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf.inputs[27].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf.inputs[28].default_value = 0.0
    # Thin Film IOR
    principled_bsdf.inputs[29].default_value = 1.3300000429153442

    # node Math
    math_1 = rockshader.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = "MULTIPLY"
    math_1.use_clamp = False
    # Value_001
    math_1.inputs[1].default_value = 10.0

    # node Group.001
    group_001 = rockshader.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random_x4___mat
    # Socket_5
    group_001.inputs[0].default_value = 0.5213124752044678

    # node Voronoi Texture
    voronoi_texture = rockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = "EUCLIDEAN"
    voronoi_texture.feature = "F1"
    voronoi_texture.normalize = True
    voronoi_texture.voronoi_dimensions = "4D"
    # Detail
    voronoi_texture.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture.inputs[4].default_value = 1.0
    # Lacunarity
    voronoi_texture.inputs[5].default_value = 2.0
    # Randomness
    voronoi_texture.inputs[8].default_value = 1.0

    # node Bump.002
    bump_002 = rockshader.nodes.new("ShaderNodeBump")
    bump_002.name = "Bump.002"
    bump_002.invert = False
    # Distance
    bump_002.inputs[1].default_value = 1.0

    # node Color Ramp.005
    color_ramp_005 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = "RGB"
    color_ramp_005.color_ramp.hue_interpolation = "NEAR"
    color_ramp_005.color_ramp.interpolation = "EASE"

    # initialize color ramp elements
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.0
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.15909108519554138)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Voronoi Texture.001
    voronoi_texture_001 = rockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = "EUCLIDEAN"
    voronoi_texture_001.feature = "SMOOTH_F1"
    voronoi_texture_001.normalize = True
    voronoi_texture_001.voronoi_dimensions = "4D"
    # Detail
    voronoi_texture_001.inputs[3].default_value = 0.0
    # Roughness
    voronoi_texture_001.inputs[4].default_value = 1.0
    # Lacunarity
    voronoi_texture_001.inputs[5].default_value = 2.0
    # Smoothness
    voronoi_texture_001.inputs[6].default_value = 1.0
    # Randomness
    voronoi_texture_001.inputs[8].default_value = 1.0

    # node Color Ramp.006
    color_ramp_006 = rockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006.name = "Color Ramp.006"
    color_ramp_006.color_ramp.color_mode = "RGB"
    color_ramp_006.color_ramp.hue_interpolation = "NEAR"
    color_ramp_006.color_ramp.interpolation = "CARDINAL"

    # initialize color ramp elements
    color_ramp_006.color_ramp.elements.remove(color_ramp_006.color_ramp.elements[0])
    color_ramp_006_cre_0 = color_ramp_006.color_ramp.elements[0]
    color_ramp_006_cre_0.position = 0.0
    color_ramp_006_cre_0.alpha = 1.0
    color_ramp_006_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_006_cre_1 = color_ramp_006.color_ramp.elements.new(0.13181859254837036)
    color_ramp_006_cre_1.alpha = 1.0
    color_ramp_006_cre_1.color = (1.0, 1.0, 1.0, 1.0)

    # node Math.001
    math_001_1 = rockshader.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = "DIVIDE"
    math_001_1.use_clamp = False

    # node Bump.003
    bump_003 = rockshader.nodes.new("ShaderNodeBump")
    bump_003.name = "Bump.003"
    bump_003.invert = False
    # Distance
    bump_003.inputs[1].default_value = 1.0
    # Normal
    bump_003.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Map Range.004
    map_range_004 = rockshader.nodes.new("ShaderNodeMapRange")
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
    noise_texture.parent = frame
    color_ramp.parent = frame
    noise_texture_001.parent = frame
    color_ramp_001.parent = frame
    mix.parent = frame
    mix_001.parent = frame_002
    geometry.parent = frame_001
    color_ramp_002.parent = frame_001
    mix_003.parent = frame_002
    color_ramp_004.parent = frame_003
    hue_saturation_value.parent = frame_003

    # Set locations
    group_output_1.location = (2044.083740234375, -366.00262451171875)
    group_input_1.location = (-1756.011962890625, -822.6982421875)
    noise_texture.location = (-3084.742431640625, 781.9205322265625)
    mapping_001.location = (-1281.65478515625, -227.8770751953125)
    texture_coordinate_001.location = (-1471.65478515625, -236.3770751953125)
    bump.location = (1154.56298828125, -790.7999267578125)
    color_ramp.location = (-2845.918701171875, 769.3270263671875)
    noise_texture_001.location = (-3091.82958984375, 348.28857421875)
    color_ramp_001.location = (-2840.2607421875, 369.6982421875)
    mix.location = (-2463.6015625, 642.8758544921875)
    mix_001.location = (-1338.03955078125, 856.2105102539062)
    geometry.location = (-1595.263427734375, 1377.4110107421875)
    color_ramp_002.location = (-1332.5478515625, 1497.3221435546875)
    mix_003.location = (-1139.2666015625, 857.9177856445312)
    color_ramp_004.location = (-1898.9849853515625, 572.5324096679688)
    noise_texture_003.location = (233.37887573242188, -895.6905517578125)
    bump_001.location = (1390.9708251953125, -663.4024658203125)
    frame_001.location = (1076.4444580078125, -1275.853271484375)
    frame_002.location = (1587.0386962890625, -923.2500610351562)
    frame.location = (2204.56005859375, -1019.8477783203125)
    hue_saturation_value.location = (-1571.6060791015625, 569.7412719726562)
    frame_003.location = (2145.8759765625, -1014.9539794921875)
    principled_bsdf.location = (1568.39306640625, -416.8108215332031)
    math_1.location = (-1059.811279296875, -390.11346435546875)
    group_001.location = (-2127.677001953125, -45.7719612121582)
    voronoi_texture.location = (201.54551696777344, -1322.15673828125)
    bump_002.location = (925.5811157226562, -915.0869750976562)
    color_ramp_005.location = (387.2950439453125, -1225.90478515625)
    voronoi_texture_001.location = (209.61325073242188, -1741.732666015625)
    color_ramp_006.location = (464.92108154296875, -1571.82275390625)
    math_001_1.location = (-162.15603637695312, -1974.9114990234375)
    bump_003.location = (761.9248046875, -1172.5350341796875)
    map_range_004.location = (-1697.904541015625, -193.53184509277344)
    group_002.location = (-1084.7215576171875, -1829.677734375)
    math_002.location = (-578.4093627929688, -1308.6357421875)
    math_003.location = (-452.7193603515625, -1984.625732421875)
    math_004.location = (-351.4325866699219, -1473.386962890625)

    # initialize rockshader links
    # mapping_001.Vector -> noise_texture_001.Vector
    rockshader.links.new(mapping_001.outputs[0], noise_texture_001.inputs[0])
    # noise_texture_001.Fac -> color_ramp_001.Fac
    rockshader.links.new(noise_texture_001.outputs[0], color_ramp_001.inputs[0])
    # color_ramp_001.Color -> mix.B
    rockshader.links.new(color_ramp_001.outputs[0], mix.inputs[7])
    # color_ramp_004.Color -> hue_saturation_value.Color
    rockshader.links.new(color_ramp_004.outputs[0], hue_saturation_value.inputs[4])
    # mix_001.Result -> mix_003.A
    rockshader.links.new(mix_001.outputs[2], mix_003.inputs[6])
    # mix_003.Result -> principled_bsdf.Base Color
    rockshader.links.new(mix_003.outputs[2], principled_bsdf.inputs[0])
    # color_ramp_002.Color -> mix_003.Factor
    rockshader.links.new(color_ramp_002.outputs[0], mix_003.inputs[0])
    # hue_saturation_value.Color -> principled_bsdf.Roughness
    rockshader.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    # color_ramp.Color -> mix.A
    rockshader.links.new(color_ramp.outputs[0], mix.inputs[6])
    # mix.Result -> color_ramp_004.Fac
    rockshader.links.new(mix.outputs[2], color_ramp_004.inputs[0])
    # mapping_001.Vector -> noise_texture_003.Vector
    rockshader.links.new(mapping_001.outputs[0], noise_texture_003.inputs[0])
    # bump.Normal -> bump_001.Normal
    rockshader.links.new(bump.outputs[0], bump_001.inputs[3])
    # mix.Result -> mix_001.Factor
    rockshader.links.new(mix.outputs[2], mix_001.inputs[0])
    # mapping_001.Vector -> noise_texture.Vector
    rockshader.links.new(mapping_001.outputs[0], noise_texture.inputs[0])
    # geometry.Pointiness -> color_ramp_002.Fac
    rockshader.links.new(geometry.outputs[7], color_ramp_002.inputs[0])
    # mix.Result -> bump_001.Height
    rockshader.links.new(mix.outputs[2], bump_001.inputs[2])
    # noise_texture.Fac -> color_ramp.Fac
    rockshader.links.new(noise_texture.outputs[0], color_ramp.inputs[0])
    # texture_coordinate_001.Object -> mapping_001.Vector
    rockshader.links.new(texture_coordinate_001.outputs[3], mapping_001.inputs[0])
    # principled_bsdf.BSDF -> group_output_1.BSDF
    rockshader.links.new(principled_bsdf.outputs[0], group_output_1.inputs[0])
    # group_input_1.Scale -> mapping_001.Scale
    rockshader.links.new(group_input_1.outputs[0], mapping_001.inputs[3])
    # group_input_1.Rock Color 1 -> mix_001.A
    rockshader.links.new(group_input_1.outputs[1], mix_001.inputs[6])
    # group_input_1.Rock Color 2 -> mix_001.B
    rockshader.links.new(group_input_1.outputs[2], mix_001.inputs[7])
    # group_input_1.Edge Lightness -> mix_003.B
    rockshader.links.new(group_input_1.outputs[3], mix_003.inputs[7])
    # group_input_1.Noise Detail -> noise_texture.Detail
    rockshader.links.new(group_input_1.outputs[5], noise_texture.inputs[3])
    # group_input_1.Noise Roughness -> noise_texture.Roughness
    rockshader.links.new(group_input_1.outputs[6], noise_texture.inputs[4])
    # group_input_1.Noise Detail -> noise_texture_001.Detail
    rockshader.links.new(group_input_1.outputs[5], noise_texture_001.inputs[3])
    # group_input_1.Noise Roughness -> noise_texture_001.Roughness
    rockshader.links.new(group_input_1.outputs[6], noise_texture_001.inputs[4])
    # group_input_1.Rughness -> hue_saturation_value.Value
    rockshader.links.new(group_input_1.outputs[9], hue_saturation_value.inputs[2])
    # group_input_1.Noise Bump  Strength -> bump.Strength
    rockshader.links.new(group_input_1.outputs[11], bump.inputs[0])
    # group_input_1.Noise Bump Scale -> noise_texture_003.Scale
    rockshader.links.new(group_input_1.outputs[10], noise_texture_003.inputs[2])
    # group_input_1.Detailed Noise Bump Strength -> bump_001.Strength
    rockshader.links.new(group_input_1.outputs[12], bump_001.inputs[0])
    # group_input_1.Noise Scale -> noise_texture_001.Scale
    rockshader.links.new(group_input_1.outputs[4], noise_texture_001.inputs[2])
    # group_input_1.Noise scale mixer -> mix.Factor
    rockshader.links.new(group_input_1.outputs[14], mix.inputs[0])
    # group_input_1.Noise Scale -> math_1.Value
    rockshader.links.new(group_input_1.outputs[4], math_1.inputs[0])
    # math_1.Value -> noise_texture.Scale
    rockshader.links.new(math_1.outputs[0], noise_texture.inputs[2])
    # group_input_1.Noise Bump Roughness -> noise_texture_003.Roughness
    rockshader.links.new(group_input_1.outputs[15], noise_texture_003.inputs[4])
    # group_001.4 -> noise_texture_001.W
    rockshader.links.new(group_001.outputs[4], noise_texture_001.inputs[1])
    # group_001.3 -> noise_texture.W
    rockshader.links.new(group_001.outputs[3], noise_texture.inputs[1])
    # group_001.1 -> noise_texture_003.W
    rockshader.links.new(group_001.outputs[1], noise_texture_003.inputs[1])
    # bump_001.Normal -> principled_bsdf.Normal
    rockshader.links.new(bump_001.outputs[0], principled_bsdf.inputs[5])
    # noise_texture_003.Fac -> bump.Height
    rockshader.links.new(noise_texture_003.outputs[0], bump.inputs[2])
    # mapping_001.Vector -> voronoi_texture.Vector
    rockshader.links.new(mapping_001.outputs[0], voronoi_texture.inputs[0])
    # group_001.1 -> voronoi_texture.W
    rockshader.links.new(group_001.outputs[1], voronoi_texture.inputs[1])
    # color_ramp_005.Color -> bump_002.Height
    rockshader.links.new(color_ramp_005.outputs[0], bump_002.inputs[2])
    # bump_002.Normal -> bump.Normal
    rockshader.links.new(bump_002.outputs[0], bump.inputs[3])
    # voronoi_texture.Distance -> color_ramp_005.Fac
    rockshader.links.new(voronoi_texture.outputs[0], color_ramp_005.inputs[0])
    # group_input_1.Voronoi Bump Scale -> voronoi_texture.Scale
    rockshader.links.new(group_input_1.outputs[16], voronoi_texture.inputs[2])
    # mapping_001.Vector -> voronoi_texture_001.Vector
    rockshader.links.new(mapping_001.outputs[0], voronoi_texture_001.inputs[0])
    # group_001.1 -> voronoi_texture_001.W
    rockshader.links.new(group_001.outputs[1], voronoi_texture_001.inputs[1])
    # math_001_1.Value -> voronoi_texture_001.Scale
    rockshader.links.new(math_001_1.outputs[0], voronoi_texture_001.inputs[2])
    # voronoi_texture_001.Distance -> color_ramp_006.Fac
    rockshader.links.new(voronoi_texture_001.outputs[0], color_ramp_006.inputs[0])
    # group_input_1.Voronoi Bump Scale -> math_001_1.Value
    rockshader.links.new(group_input_1.outputs[16], math_001_1.inputs[0])
    # color_ramp_006.Color -> bump_003.Height
    rockshader.links.new(color_ramp_006.outputs[0], bump_003.inputs[2])
    # bump_003.Normal -> bump_002.Normal
    rockshader.links.new(bump_003.outputs[0], bump_002.inputs[3])
    # map_range_004.Result -> mapping_001.Location
    rockshader.links.new(map_range_004.outputs[0], mapping_001.inputs[1])
    # group_001.0 -> map_range_004.Value
    rockshader.links.new(group_001.outputs[0], map_range_004.inputs[0])
    # group_002.0 -> math_002.Value
    rockshader.links.new(group_002.outputs[0], math_002.inputs[1])
    # group_input_1.Voronoi Bump Strength -> math_002.Value
    rockshader.links.new(group_input_1.outputs[17], math_002.inputs[0])
    # math_002.Value -> bump_003.Strength
    rockshader.links.new(math_002.outputs[0], bump_003.inputs[0])
    # group_001.2 -> group_002.Seed
    rockshader.links.new(group_001.outputs[2], group_002.inputs[0])
    # math_003.Value -> math_001_1.Value
    rockshader.links.new(math_003.outputs[0], math_001_1.inputs[1])
    # group_002.1 -> math_003.Value
    rockshader.links.new(group_002.outputs[1], math_003.inputs[0])
    # group_input_1.Voronoi Bump Strength -> math_004.Value
    rockshader.links.new(group_input_1.outputs[17], math_004.inputs[0])
    # group_002.2 -> math_004.Value
    rockshader.links.new(group_002.outputs[2], math_004.inputs[1])
    # math_004.Value -> bump_002.Strength
    rockshader.links.new(math_004.outputs[0], bump_002.inputs[0])
    return rockshader


rockshader = rockshader_node_group()


# initialize LunarRock node group
def lunarrock_node_group():
    lunarrock = mat.node_tree
    # start with a clean node tree
    for node in lunarrock.nodes:
        lunarrock.nodes.remove(node)
    lunarrock.color_tag = "NONE"
    lunarrock.description = ""

    # lunarrock interface

    # initialize lunarrock nodes
    # node Material Output
    material_output = lunarrock.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = "ALL"
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0

    # node Group.006
    group_006 = lunarrock.nodes.new("ShaderNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = rockshader
    # Socket_1
    group_006.inputs[0].default_value = 4.0
    # Socket_5
    group_006.inputs[4].default_value = 7.0
    # Socket_6
    group_006.inputs[5].default_value = 15.0
    # Socket_7
    group_006.inputs[6].default_value = 0.25
    # Socket_8
    group_006.inputs[7].default_value = 5.0
    # Socket_9
    group_006.inputs[8].default_value = 0.800000011920929
    # Socket_10
    group_006.inputs[9].default_value = 1.0
    # Socket_11
    group_006.inputs[10].default_value = 15.0
    # Socket_12
    group_006.inputs[11].default_value = 0.05000000074505806
    # Socket_13
    group_006.inputs[12].default_value = 0.25
    # Socket_14
    group_006.inputs[13].default_value = 0.75
    # Socket_15
    group_006.inputs[14].default_value = 0.009999999776482582
    # Socket_16
    group_006.inputs[15].default_value = 1.0
    # Socket_17
    group_006.inputs[16].default_value = 20.0
    # Socket_18
    group_006.inputs[17].default_value = 0.75

    # node Combine Color.004
    combine_color_004 = lunarrock.nodes.new("ShaderNodeCombineColor")
    combine_color_004.name = "Combine Color.004"
    combine_color_004.mode = "HSV"
    # Red
    combine_color_004.inputs[0].default_value = 0.0
    # Green
    combine_color_004.inputs[1].default_value = 0.0

    # node Map Range.009
    map_range_009 = lunarrock.nodes.new("ShaderNodeMapRange")
    map_range_009.name = "Map Range.009"
    map_range_009.clamp = True
    map_range_009.data_type = "FLOAT"
    map_range_009.interpolation_type = "LINEAR"
    # From Min
    map_range_009.inputs[1].default_value = 0.0
    # From Max
    map_range_009.inputs[2].default_value = 1.0
    # To Min
    map_range_009.inputs[3].default_value = 0.02500000037252903
    # To Max
    map_range_009.inputs[4].default_value = 0.10000000149011612

    # node Combine Color.005
    combine_color_005 = lunarrock.nodes.new("ShaderNodeCombineColor")
    combine_color_005.name = "Combine Color.005"
    combine_color_005.mode = "HSV"
    # Red
    combine_color_005.inputs[0].default_value = 0.0
    # Green
    combine_color_005.inputs[1].default_value = 0.0

    # node Map Range.010
    map_range_010 = lunarrock.nodes.new("ShaderNodeMapRange")
    map_range_010.name = "Map Range.010"
    map_range_010.clamp = True
    map_range_010.data_type = "FLOAT"
    map_range_010.interpolation_type = "LINEAR"
    # From Min
    map_range_010.inputs[1].default_value = 0.0
    # From Max
    map_range_010.inputs[2].default_value = 1.0
    # To Min
    map_range_010.inputs[3].default_value = 0.0
    # To Max
    map_range_010.inputs[4].default_value = 0.02500000037252903

    # node Group
    group = lunarrock.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = random_x4___mat
    # Socket_5
    group.inputs[0].default_value = 0.5123251080513

    # node Combine Color.001
    combine_color_001 = lunarrock.nodes.new("ShaderNodeCombineColor")
    combine_color_001.name = "Combine Color.001"
    combine_color_001.mode = "HSV"
    # Red
    combine_color_001.inputs[0].default_value = 0.0
    # Green
    combine_color_001.inputs[1].default_value = 0.0

    # node Map Range.005
    map_range_005 = lunarrock.nodes.new("ShaderNodeMapRange")
    map_range_005.name = "Map Range.005"
    map_range_005.clamp = True
    map_range_005.data_type = "FLOAT"
    map_range_005.interpolation_type = "LINEAR"
    # From Min
    map_range_005.inputs[1].default_value = 0.0
    # From Max
    map_range_005.inputs[2].default_value = 1.0
    # To Min
    map_range_005.inputs[3].default_value = 0.20000000298023224
    # To Max
    map_range_005.inputs[4].default_value = 0.3499999940395355

    # Set locations
    material_output.location = (-63.728790283203125, -75.2525634765625)
    group_006.location = (-555.7568969726562, 120.46104431152344)
    combine_color_004.location = (-975.1624145507812, 48.7264404296875)
    map_range_009.location = (-1165.162353515625, 97.7264404296875)
    combine_color_005.location = (-971.2743530273438, -249.97727966308594)
    map_range_010.location = (-1165.162353515625, -265.1905517578125)
    group.location = (-1451.4873046875, -12.02740478515625)
    combine_color_001.location = (-972.9628295898438, 405.77777099609375)
    map_range_005.location = (-1162.962890625, 454.77777099609375)

    # initialize lunarrock links
    # map_range_009.Result -> combine_color_004.Blue
    lunarrock.links.new(map_range_009.outputs[0], combine_color_004.inputs[2])
    # map_range_010.Result -> combine_color_005.Blue
    lunarrock.links.new(map_range_010.outputs[0], combine_color_005.inputs[2])
    # group.1 -> map_range_009.Value
    lunarrock.links.new(group.outputs[1], map_range_009.inputs[0])
    # group.2 -> map_range_010.Value
    lunarrock.links.new(group.outputs[2], map_range_010.inputs[0])
    # combine_color_005.Color -> group_006.Rock Color 2
    lunarrock.links.new(combine_color_005.outputs[0], group_006.inputs[2])
    # combine_color_004.Color -> group_006.Rock Color 1
    lunarrock.links.new(combine_color_004.outputs[0], group_006.inputs[1])
    # map_range_005.Result -> combine_color_001.Blue
    lunarrock.links.new(map_range_005.outputs[0], combine_color_001.inputs[2])
    # combine_color_001.Color -> group_006.Edge Lightness
    lunarrock.links.new(combine_color_001.outputs[0], group_006.inputs[3])
    # group.0 -> map_range_005.Value
    lunarrock.links.new(group.outputs[0], map_range_005.inputs[0])
    # group_006.BSDF -> material_output.Surface
    lunarrock.links.new(group_006.outputs[0], material_output.inputs[0])
    return lunarrock


lunarrock = lunarrock_node_group()
