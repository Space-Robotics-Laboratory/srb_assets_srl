import bpy


# initialize random__uniform_ node group
def random__uniform__node_group():
    random__uniform_ = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="Random (Uniform)"
    )

    random__uniform_.color_tag = "NONE"
    random__uniform_.description = ""

    # random__uniform_ interface
    # Socket Value
    value_socket = random__uniform_.interface.new_socket(
        name="Value", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e38
    value_socket.max_value = 3.4028234663852886e38
    value_socket.subtype = "NONE"
    value_socket.attribute_domain = "POINT"

    # Socket Min
    min_socket = random__uniform_.interface.new_socket(
        name="Min", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    min_socket.default_value = 0.0
    min_socket.min_value = -3.4028234663852886e38
    min_socket.max_value = 3.4028234663852886e38
    min_socket.subtype = "NONE"
    min_socket.attribute_domain = "POINT"

    # Socket Max
    max_socket = random__uniform_.interface.new_socket(
        name="Max", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    max_socket.default_value = 1.0
    max_socket.min_value = -3.4028234663852886e38
    max_socket.max_value = 3.4028234663852886e38
    max_socket.subtype = "NONE"
    max_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket = random__uniform_.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = "NONE"
    seed_socket.attribute_domain = "POINT"
    seed_socket.hide_value = True

    # Socket Offset
    offset_socket = random__uniform_.interface.new_socket(
        name="Offset", in_out="INPUT", socket_type="NodeSocketInt"
    )
    offset_socket.default_value = 0
    offset_socket.min_value = 0
    offset_socket.max_value = 2147483647
    offset_socket.subtype = "NONE"
    offset_socket.attribute_domain = "POINT"

    # initialize random__uniform_ nodes
    # node Group Output
    group_output = random__uniform_.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # node Group Input
    group_input = random__uniform_.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # node Random Value.011
    random_value_011 = random__uniform_.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = "FLOAT"

    # Set locations
    group_output.location = (190.0, 0.0)
    group_input.location = (-200.0, 0.0)
    random_value_011.location = (0.0, 0.0)

    # initialize random__uniform_ links
    # random_value_011.Value -> group_output.Value
    random__uniform_.links.new(random_value_011.outputs[1], group_output.inputs[0])
    # group_input.Min -> random_value_011.Min
    random__uniform_.links.new(group_input.outputs[0], random_value_011.inputs[2])
    # group_input.Max -> random_value_011.Max
    random__uniform_.links.new(group_input.outputs[1], random_value_011.inputs[3])
    # group_input.Offset -> random_value_011.ID
    random__uniform_.links.new(group_input.outputs[3], random_value_011.inputs[7])
    # group_input.Seed -> random_value_011.Seed
    random__uniform_.links.new(group_input.outputs[2], random_value_011.inputs[8])
    return random__uniform_


random__uniform_ = random__uniform__node_group()


# initialize random__normal_ node group
def random__normal__node_group():
    random__normal_ = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="Random (Normal)"
    )

    random__normal_.color_tag = "NONE"
    random__normal_.description = ""

    # random__normal_ interface
    # Socket Value
    value_socket_1 = random__normal_.interface.new_socket(
        name="Value", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    value_socket_1.default_value = 0.0
    value_socket_1.min_value = -3.4028234663852886e38
    value_socket_1.max_value = 3.4028234663852886e38
    value_socket_1.subtype = "NONE"
    value_socket_1.attribute_domain = "POINT"

    # Socket Non-Negative
    non_negative_socket = random__normal_.interface.new_socket(
        name="Non-Negative", in_out="INPUT", socket_type="NodeSocketBool"
    )
    non_negative_socket.default_value = True
    non_negative_socket.attribute_domain = "POINT"

    # Socket Mean
    mean_socket = random__normal_.interface.new_socket(
        name="Mean", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    mean_socket.default_value = 0.0
    mean_socket.min_value = -3.4028234663852886e38
    mean_socket.max_value = 3.4028234663852886e38
    mean_socket.subtype = "NONE"
    mean_socket.attribute_domain = "POINT"

    # Socket Std. Dev.
    std__dev__socket = random__normal_.interface.new_socket(
        name="Std. Dev.", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    std__dev__socket.default_value = 1.0
    std__dev__socket.min_value = 0.0
    std__dev__socket.max_value = 3.4028234663852886e38
    std__dev__socket.subtype = "NONE"
    std__dev__socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_1 = random__normal_.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket_1.default_value = 0
    seed_socket_1.min_value = 0
    seed_socket_1.max_value = 2147483647
    seed_socket_1.subtype = "NONE"
    seed_socket_1.attribute_domain = "POINT"
    seed_socket_1.hide_value = True

    # Socket Offset
    offset_socket_1 = random__normal_.interface.new_socket(
        name="Offset", in_out="INPUT", socket_type="NodeSocketInt"
    )
    offset_socket_1.default_value = 0
    offset_socket_1.min_value = 0
    offset_socket_1.max_value = 2147483647
    offset_socket_1.subtype = "NONE"
    offset_socket_1.attribute_domain = "POINT"

    # initialize random__normal_ nodes
    # node Frame
    frame = random__normal_.nodes.new("NodeFrame")
    frame.label = "2 * pi * U_2"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # node Frame.003
    frame_003 = random__normal_.nodes.new("NodeFrame")
    frame_003.label = "X_1"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # node Frame.001
    frame_001 = random__normal_.nodes.new("NodeFrame")
    frame_001.label = "sqrt(-2 * ln(U_1))"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # node Math.002
    math_002 = random__normal_.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = "MULTIPLY"
    math_002.use_clamp = False
    # Value_001
    math_002.inputs[1].default_value = 6.2831854820251465

    # node Random Value.001
    random_value_001 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_001.label = "U_2"
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = "FLOAT"
    # Min_001
    random_value_001.inputs[2].default_value = 0.0
    # Max_001
    random_value_001.inputs[3].default_value = 1.0

    # node Math.010
    math_010 = random__normal_.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = "ADD"
    math_010.use_clamp = False
    math_010.inputs[1].hide = True
    math_010.inputs[2].hide = True
    # Value_001
    math_010.inputs[1].default_value = 1.0

    # node Math.005
    math_005 = random__normal_.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = "MULTIPLY"
    math_005.use_clamp = False

    # node Math.004
    math_004 = random__normal_.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = "COSINE"
    math_004.use_clamp = False

    # node Math.008
    math_008 = random__normal_.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = "MULTIPLY"
    math_008.use_clamp = False

    # node Math.007
    math_007 = random__normal_.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = "ADD"
    math_007.use_clamp = False

    # node Math
    math = random__normal_.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = "LOGARITHM"
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 2.7182817459106445

    # node Random Value.002
    random_value_002 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_002.label = "U_1"
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = "FLOAT"
    # Min_001
    random_value_002.inputs[2].default_value = 0.0
    # Max_001
    random_value_002.inputs[3].default_value = 1.0

    # node Math.001
    math_001 = random__normal_.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = "MULTIPLY"
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = -2.0

    # node Math.003
    math_003 = random__normal_.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = "SQRT"
    math_003.use_clamp = False

    # node Group Output
    group_output_1 = random__normal_.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # node Group Input
    group_input_1 = random__normal_.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    # node Switch
    switch = random__normal_.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = "FLOAT"

    # node Math.006
    math_006 = random__normal_.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = "MAXIMUM"
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = 0.0

    # Set parents
    math_002.parent = frame
    random_value_001.parent = frame
    math_010.parent = frame
    math_005.parent = frame_003
    math_004.parent = frame_003
    math.parent = frame_001
    random_value_002.parent = frame_001
    math_001.parent = frame_001
    math_003.parent = frame_001

    # Set locations
    frame.location = (-789.8994140625, -466.3039245605469)
    frame_003.location = (-189.27259826660156, -312.6241455078125)
    frame_001.location = (-1020.868408203125, -235.92041015625)
    math_002.location = (138.8717041015625, -30.349945068359375)
    random_value_001.location = (-51.1282958984375, -20.849945068359375)
    math_010.location = (-241.1282958984375, -137.92230224609375)
    math_005.location = (197.912353515625, -20.78594970703125)
    math_004.location = (7.912353515625, -110.67535400390625)
    math_008.location = (210.5360565185547, -105.03559112548828)
    math_007.location = (400.53607177734375, 29.03577995300293)
    math.location = (177.51742553710938, -9.365585327148438)
    random_value_002.location = (-12.482574462890625, 0.1344146728515625)
    math_001.location = (367.5174255371094, -9.365585327148438)
    math_003.location = (557.5174560546875, -20.365585327148438)
    group_output_1.location = (970.5360717773438, -8.96422004699707)
    group_input_1.location = (-1399.3758544921875, -91.58724975585938)
    switch.location = (780.5360717773438, 26.53577995300293)
    math_006.location = (590.5360717773438, -88.39610290527344)

    # initialize random__normal_ links
    # random_value_002.Value -> math.Value
    random__normal_.links.new(random_value_002.outputs[1], math.inputs[0])
    # math.Value -> math_001.Value
    random__normal_.links.new(math.outputs[0], math_001.inputs[0])
    # random_value_001.Value -> math_002.Value
    random__normal_.links.new(random_value_001.outputs[1], math_002.inputs[0])
    # math_002.Value -> math_004.Value
    random__normal_.links.new(math_002.outputs[0], math_004.inputs[0])
    # math_003.Value -> math_005.Value
    random__normal_.links.new(math_003.outputs[0], math_005.inputs[0])
    # group_input_1.Seed -> random_value_002.Seed
    random__normal_.links.new(group_input_1.outputs[3], random_value_002.inputs[8])
    # group_input_1.Seed -> math_010.Value
    random__normal_.links.new(group_input_1.outputs[3], math_010.inputs[0])
    # math_010.Value -> random_value_001.Seed
    random__normal_.links.new(math_010.outputs[0], random_value_001.inputs[8])
    # group_input_1.Std. Dev. -> math_008.Value
    random__normal_.links.new(group_input_1.outputs[2], math_008.inputs[0])
    # group_input_1.Mean -> math_007.Value
    random__normal_.links.new(group_input_1.outputs[1], math_007.inputs[0])
    # math_008.Value -> math_007.Value
    random__normal_.links.new(math_008.outputs[0], math_007.inputs[1])
    # math_005.Value -> math_008.Value
    random__normal_.links.new(math_005.outputs[0], math_008.inputs[1])
    # math_004.Value -> math_005.Value
    random__normal_.links.new(math_004.outputs[0], math_005.inputs[1])
    # math_001.Value -> math_003.Value
    random__normal_.links.new(math_001.outputs[0], math_003.inputs[0])
    # group_input_1.Offset -> random_value_001.ID
    random__normal_.links.new(group_input_1.outputs[4], random_value_001.inputs[7])
    # group_input_1.Offset -> random_value_002.ID
    random__normal_.links.new(group_input_1.outputs[4], random_value_002.inputs[7])
    # group_input_1.Non-Negative -> switch.Switch
    random__normal_.links.new(group_input_1.outputs[0], switch.inputs[0])
    # math_007.Value -> math_006.Value
    random__normal_.links.new(math_007.outputs[0], math_006.inputs[0])
    # switch.Output -> group_output_1.Value
    random__normal_.links.new(switch.outputs[0], group_output_1.inputs[0])
    # math_007.Value -> switch.False
    random__normal_.links.new(math_007.outputs[0], switch.inputs[1])
    # math_006.Value -> switch.True
    random__normal_.links.new(math_006.outputs[0], switch.inputs[2])
    return random__normal_


random__normal_ = random__normal__node_group()


# initialize martianrock node group
def martianrock_node_group():
    martianrock = bpy.data.node_groups.new(type="GeometryNodeTree", name="MartianRock")

    martianrock.color_tag = "GEOMETRY"
    martianrock.description = ""

    martianrock.is_modifier = True

    # martianrock interface
    # Socket Geometry
    geometry_socket = martianrock.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_2 = martianrock.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket_2.default_value = 0
    seed_socket_2.min_value = 0
    seed_socket_2.max_value = 2147483647
    seed_socket_2.subtype = "NONE"
    seed_socket_2.attribute_domain = "POINT"
    seed_socket_2.force_non_field = True

    # Socket Subdivisions
    subdivisions_socket = martianrock.interface.new_socket(
        name="Subdivisions", in_out="INPUT", socket_type="NodeSocketInt"
    )
    subdivisions_socket.default_value = 4
    subdivisions_socket.min_value = 0
    subdivisions_socket.max_value = 10
    subdivisions_socket.subtype = "NONE"
    subdivisions_socket.attribute_domain = "POINT"
    subdivisions_socket.force_non_field = True

    # Socket Scale
    scale_socket = martianrock.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketVector"
    )
    scale_socket.default_value = (1.0, 1.0, 1.0)
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e38
    scale_socket.subtype = "XYZ"
    scale_socket.attribute_domain = "POINT"
    scale_socket.force_non_field = True

    # Socket Scale STD
    scale_std_socket = martianrock.interface.new_socket(
        name="Scale STD", in_out="INPUT", socket_type="NodeSocketVector"
    )
    scale_std_socket.default_value = (0.0, 0.0, 0.0)
    scale_std_socket.min_value = 0.0
    scale_std_socket.max_value = 3.4028234663852886e38
    scale_std_socket.subtype = "XYZ"
    scale_std_socket.attribute_domain = "POINT"
    scale_std_socket.force_non_field = True

    # Socket Horizontal Cut
    horizontal_cut_socket = martianrock.interface.new_socket(
        name="Horizontal Cut", in_out="INPUT", socket_type="NodeSocketBool"
    )
    horizontal_cut_socket.default_value = False
    horizontal_cut_socket.attribute_domain = "POINT"
    horizontal_cut_socket.force_non_field = True

    # Socket Horizontal Cut Offset
    horizontal_cut_offset_socket = martianrock.interface.new_socket(
        name="Horizontal Cut Offset", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    horizontal_cut_offset_socket.default_value = 0.0
    horizontal_cut_offset_socket.min_value = -3.4028234663852886e38
    horizontal_cut_offset_socket.max_value = 3.4028234663852886e38
    horizontal_cut_offset_socket.subtype = "DISTANCE"
    horizontal_cut_offset_socket.attribute_domain = "POINT"
    horizontal_cut_offset_socket.force_non_field = True

    # initialize martianrock nodes
    # node Group Input
    group_input_2 = martianrock.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"

    # node Group Output
    group_output_2 = martianrock.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True

    # node Set Material
    set_material = martianrock.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    # Selection
    set_material.inputs[1].default_value = True
    if "MartianRock" in bpy.data.materials:
        set_material.inputs[2].default_value = bpy.data.materials["MartianRock"]

    # node Cube
    cube = martianrock.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    # Size
    cube.inputs[0].default_value = (1.0, 1.0, 1.0)
    # Vertices X
    cube.inputs[1].default_value = 2
    # Vertices Y
    cube.inputs[2].default_value = 2
    # Vertices Z
    cube.inputs[3].default_value = 2

    # node Subdivision Surface
    subdivision_surface = martianrock.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.boundary_smooth = "ALL"
    subdivision_surface.uv_smooth = "PRESERVE_BOUNDARIES"

    # node Set Position
    set_position = martianrock.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].hide = True
    set_position.inputs[3].hide = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Voronoi Texture
    voronoi_texture = martianrock.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = "EUCLIDEAN"
    voronoi_texture.feature = "SMOOTH_F1"
    voronoi_texture.normalize = True
    voronoi_texture.voronoi_dimensions = "4D"
    # Vector
    voronoi_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Smoothness
    voronoi_texture.inputs[6].default_value = 0.0
    # Randomness
    voronoi_texture.inputs[8].default_value = 1.0

    # node Vector Math
    vector_math = martianrock.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = "MULTIPLY"

    # node Position
    position = martianrock.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    # node Map Range
    map_range = martianrock.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = False
    map_range.data_type = "FLOAT"
    map_range.interpolation_type = "LINEAR"
    # From Min
    map_range.inputs[1].default_value = 0.0
    # From Max
    map_range.inputs[2].default_value = 1.0
    # To Min
    map_range.inputs[3].default_value = 0.3333333432674408
    # To Max
    map_range.inputs[4].default_value = 1.0

    # node Set Position.001
    set_position_001 = martianrock.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[1].hide = True
    set_position_001.inputs[3].hide = True
    # Selection
    set_position_001.inputs[1].default_value = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Vector Math.001
    vector_math_001 = martianrock.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = "MULTIPLY"

    # node Position.001
    position_001 = martianrock.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    # node Noise Texture
    noise_texture = martianrock.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = "4D"
    noise_texture.noise_type = "FBM"
    noise_texture.normalize = True
    # Vector
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Detail
    noise_texture.inputs[3].default_value = 15.0

    # node Set Shade Smooth
    set_shade_smooth = martianrock.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = "FACE"
    # Selection
    set_shade_smooth.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    # node Frame
    frame_1 = martianrock.nodes.new("NodeFrame")
    frame_1.name = "Frame"
    frame_1.label_size = 20
    frame_1.shrink = True

    # node Frame.001
    frame_001_1 = martianrock.nodes.new("NodeFrame")
    frame_001_1.name = "Frame.001"
    frame_001_1.hide = True
    frame_001_1.label_size = 20
    frame_001_1.shrink = True

    # node Frame.002
    frame_002 = martianrock.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # node Reroute.001
    reroute_001 = martianrock.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    # node Transform Geometry
    transform_geometry = martianrock.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = "COMPONENTS"
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[4].hide = True
    # Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Reroute.002
    reroute_002 = martianrock.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    # node Attribute Statistic
    attribute_statistic = martianrock.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = "FLOAT_VECTOR"
    attribute_statistic.domain = "POINT"
    attribute_statistic.inputs[1].hide = True
    attribute_statistic.outputs[0].hide = True
    attribute_statistic.outputs[1].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True
    # Selection
    attribute_statistic.inputs[1].default_value = True

    # node Position.002
    position_002 = martianrock.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"

    # node Reroute.003
    reroute_003 = martianrock.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    # node Vector Math.002
    vector_math_002 = martianrock.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = "DIVIDE"
    # Vector
    vector_math_002.inputs[0].default_value = (1.0, 1.0, 1.0)

    # node Vector Math.003
    vector_math_003 = martianrock.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = "ADD"

    # node Vector Math.004
    vector_math_004 = martianrock.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = "SCALE"
    # Scale
    vector_math_004.inputs[3].default_value = -0.5

    # node Group
    group = martianrock.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = random__normal_
    # Socket_1
    group.inputs[0].default_value = True
    # Socket_2
    group.inputs[1].default_value = 2.25
    # Socket_3
    group.inputs[2].default_value = 0.3333333432674408
    # Socket_5
    group.inputs[4].default_value = 9799

    # node Group.001
    group_001 = martianrock.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random__uniform_
    # Socket_1
    group_001.inputs[0].default_value = -100000000.0
    # Socket_2
    group_001.inputs[1].default_value = 1000000000.0
    # Socket_4
    group_001.inputs[3].default_value = 10074

    # node Group.002
    group_002 = martianrock.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random__normal_
    # Socket_1
    group_002.inputs[0].default_value = True
    # Socket_2
    group_002.inputs[1].default_value = 1.0
    # Socket_3
    group_002.inputs[2].default_value = 0.25
    # Socket_5
    group_002.inputs[4].default_value = 8856

    # node Group.004
    group_004 = martianrock.nodes.new("GeometryNodeGroup")
    group_004.name = "Group.004"
    group_004.node_tree = random__normal_
    # Socket_1
    group_004.inputs[0].default_value = True
    # Socket_2
    group_004.inputs[1].default_value = 1.25
    # Socket_3
    group_004.inputs[2].default_value = 0.25
    # Socket_5
    group_004.inputs[4].default_value = 2182

    # node Float Curve
    float_curve = martianrock.nodes.new("ShaderNodeFloatCurve")
    float_curve.name = "Float Curve"
    # mapping settings
    float_curve.mapping.extend = "EXTRAPOLATED"
    float_curve.mapping.tone = "STANDARD"
    float_curve.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve.mapping.clip_min_x = 0.0
    float_curve.mapping.clip_min_y = 0.0
    float_curve.mapping.clip_max_x = 1.0
    float_curve.mapping.clip_max_y = 1.0
    float_curve.mapping.use_clip = True
    # curve 0
    float_curve_curve_0 = float_curve.mapping.curves[0]
    float_curve_curve_0_point_0 = float_curve_curve_0.points[0]
    float_curve_curve_0_point_0.location = (0.0, 0.0)
    float_curve_curve_0_point_0.handle_type = "AUTO"
    float_curve_curve_0_point_1 = float_curve_curve_0.points[1]
    float_curve_curve_0_point_1.location = (0.3333333432674408, 0.10000000149011612)
    float_curve_curve_0_point_1.handle_type = "AUTO_CLAMPED"
    float_curve_curve_0_point_2 = float_curve_curve_0.points.new(1.0, 1.0)
    float_curve_curve_0_point_2.handle_type = "AUTO"
    # update curve after changes
    float_curve.mapping.update()
    # Factor
    float_curve.inputs[0].default_value = 1.0

    # node Group.005
    group_005 = martianrock.nodes.new("GeometryNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = random__normal_
    # Socket_1
    group_005.inputs[0].default_value = True
    # Socket_2
    group_005.inputs[1].default_value = 0.25
    # Socket_3
    group_005.inputs[2].default_value = 0.10000000149011612
    # Socket_5
    group_005.inputs[4].default_value = 2227

    # node Reroute.005
    reroute_005 = martianrock.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    # node Group.003
    group_003 = martianrock.nodes.new("GeometryNodeGroup")
    group_003.name = "Group.003"
    group_003.node_tree = random__normal_
    # Socket_1
    group_003.inputs[0].default_value = True
    # Socket_2
    group_003.inputs[1].default_value = 0.15000000596046448
    # Socket_3
    group_003.inputs[2].default_value = 0.02500000037252903
    # Socket_5
    group_003.inputs[4].default_value = 21973

    # node Group.006
    group_006 = martianrock.nodes.new("GeometryNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = random__normal_
    # Socket_1
    group_006.inputs[0].default_value = True
    # Socket_2
    group_006.inputs[1].default_value = 0.20000000298023224
    # Socket_3
    group_006.inputs[2].default_value = 0.05000000074505806
    # Socket_5
    group_006.inputs[4].default_value = 14855

    # node Reroute.006
    reroute_006 = martianrock.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    # node Reroute
    reroute = martianrock.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    # node Group.007
    group_007 = martianrock.nodes.new("GeometryNodeGroup")
    group_007.name = "Group.007"
    group_007.node_tree = random__uniform_
    # Socket_1
    group_007.inputs[0].default_value = -100000000.0
    # Socket_2
    group_007.inputs[1].default_value = 1000000000.0
    # Socket_4
    group_007.inputs[3].default_value = 10781

    # node Group.008
    group_008 = martianrock.nodes.new("GeometryNodeGroup")
    group_008.name = "Group.008"
    group_008.node_tree = random__normal_
    # Socket_1
    group_008.inputs[0].default_value = True
    # Socket_2
    group_008.inputs[1].default_value = 0.07500000298023224
    # Socket_3
    group_008.inputs[2].default_value = 0.02500000037252903
    # Socket_5
    group_008.inputs[4].default_value = 3267

    # node Group.010
    group_010 = martianrock.nodes.new("GeometryNodeGroup")
    group_010.name = "Group.010"
    group_010.node_tree = random__normal_
    # Socket_1
    group_010.inputs[0].default_value = True
    # Socket_2
    group_010.inputs[1].default_value = 0.5600000023841858
    # Socket_3
    group_010.inputs[2].default_value = 0.019999999552965164
    # Socket_5
    group_010.inputs[4].default_value = 5038

    # node Group.011
    group_011 = martianrock.nodes.new("GeometryNodeGroup")
    group_011.name = "Group.011"
    group_011.node_tree = random__normal_
    # Socket_1
    group_011.inputs[0].default_value = True
    # Socket_2
    group_011.inputs[1].default_value = 2.4000000953674316
    # Socket_3
    group_011.inputs[2].default_value = 0.20000000298023224
    # Socket_5
    group_011.inputs[4].default_value = 3147

    # node Group.012
    group_012 = martianrock.nodes.new("GeometryNodeGroup")
    group_012.name = "Group.012"
    group_012.node_tree = random__normal_
    # Socket_1
    group_012.inputs[0].default_value = True
    # Socket_2
    group_012.inputs[1].default_value = 0.05000000074505806
    # Socket_3
    group_012.inputs[2].default_value = 0.009999999776482582
    # Socket_5
    group_012.inputs[4].default_value = 3622

    # node Frame.003
    frame_003_1 = martianrock.nodes.new("NodeFrame")
    frame_003_1.name = "Frame.003"
    frame_003_1.label_size = 20
    frame_003_1.shrink = True

    # node Transform Geometry.001
    transform_geometry_001 = martianrock.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = "COMPONENTS"
    transform_geometry_001.inputs[1].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[4].hide = True
    # Translation
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Random Value
    random_value = martianrock.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = "FLOAT_VECTOR"
    random_value.inputs[0].hide = True
    random_value.inputs[1].hide = True
    random_value.inputs[2].hide = True
    random_value.inputs[3].hide = True
    random_value.inputs[4].hide = True
    random_value.inputs[5].hide = True
    random_value.inputs[6].hide = True
    random_value.outputs[1].hide = True
    random_value.outputs[2].hide = True
    random_value.outputs[3].hide = True
    # Min
    random_value.inputs[0].default_value = (
        -3.1415927410125732,
        -3.1415927410125732,
        -3.1415927410125732,
    )
    # Max
    random_value.inputs[1].default_value = (
        3.1415927410125732,
        3.1415927410125732,
        3.1415927410125732,
    )

    # node Integer
    integer = martianrock.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 424242

    # node Delete Geometry
    delete_geometry = martianrock.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = "FACE"
    delete_geometry.mode = "ALL"

    # node Compare
    compare = martianrock.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = "FLOAT"
    compare.mode = "ELEMENT"
    compare.operation = "EQUAL"
    # Epsilon
    compare.inputs[12].default_value = 0.0010000000474974513

    # node Position.004
    position_004 = martianrock.nodes.new("GeometryNodeInputPosition")
    position_004.name = "Position.004"

    # node Separate XYZ.001
    separate_xyz_001 = martianrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.outputs[0].hide = True
    separate_xyz_001.outputs[1].hide = True

    # node Normal.001
    normal_001 = martianrock.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"

    # node Boolean Math
    boolean_math = martianrock.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = "AND"

    # node Separate XYZ.002
    separate_xyz_002 = martianrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.outputs[0].hide = True
    separate_xyz_002.outputs[1].hide = True

    # node Compare.001
    compare_001 = martianrock.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = "FLOAT"
    compare_001.mode = "ELEMENT"
    compare_001.operation = "EQUAL"
    # B
    compare_001.inputs[1].default_value = -1.0
    # Epsilon
    compare_001.inputs[12].default_value = 0.0010000000474974513

    # node Mesh Boolean
    mesh_boolean = martianrock.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = "DIFFERENCE"
    mesh_boolean.solver = "FLOAT"
    # Self Intersection
    mesh_boolean.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean.inputs[3].default_value = False

    # node Switch
    switch_1 = martianrock.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = "GEOMETRY"

    # node Transform Geometry.002
    transform_geometry_002 = martianrock.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = "COMPONENTS"
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[4].hide = True
    # Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Combine XYZ
    combine_xyz = martianrock.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    # X
    combine_xyz.inputs[0].default_value = 0.0
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # node Reroute.010
    reroute_010 = martianrock.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    # node Cube.001
    cube_001 = martianrock.nodes.new("GeometryNodeMeshCube")
    cube_001.name = "Cube.001"
    # Size
    cube_001.inputs[0].default_value = (2.0, 2.0, 2.0)
    # Vertices X
    cube_001.inputs[1].default_value = 2
    # Vertices Y
    cube_001.inputs[2].default_value = 2
    # Vertices Z
    cube_001.inputs[3].default_value = 2

    # node Math
    math_1 = martianrock.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = "SUBTRACT"
    math_1.use_clamp = False
    # Value_001
    math_1.inputs[1].default_value = 1.0

    # node Reroute.004
    reroute_004 = martianrock.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    # node Frame.004
    frame_004 = martianrock.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    # node Reroute.012
    reroute_012 = martianrock.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    # node Reroute.013
    reroute_013 = martianrock.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    # node Transform Geometry.003
    transform_geometry_003 = martianrock.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = "COMPONENTS"
    transform_geometry_003.inputs[1].hide = True
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[4].hide = True
    # Translation
    transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Combine XYZ.001
    combine_xyz_001 = martianrock.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"

    # node Group.009
    group_009 = martianrock.nodes.new("GeometryNodeGroup")
    group_009.name = "Group.009"
    group_009.node_tree = random__normal_
    # Socket_1
    group_009.inputs[0].default_value = True
    # Socket_5
    group_009.inputs[4].default_value = 31680

    # node Group.013
    group_013 = martianrock.nodes.new("GeometryNodeGroup")
    group_013.name = "Group.013"
    group_013.node_tree = random__normal_
    # Socket_1
    group_013.inputs[0].default_value = True
    # Socket_5
    group_013.inputs[4].default_value = 32260

    # node Group.014
    group_014 = martianrock.nodes.new("GeometryNodeGroup")
    group_014.name = "Group.014"
    group_014.node_tree = random__normal_
    # Socket_1
    group_014.inputs[0].default_value = True
    # Socket_5
    group_014.inputs[4].default_value = 40590

    # node Reroute.015
    reroute_015 = martianrock.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    # node Separate XYZ
    separate_xyz = martianrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    # node Separate XYZ.003
    separate_xyz_003 = martianrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"

    # node Reroute.017
    reroute_017 = martianrock.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    # node Reroute.018
    reroute_018 = martianrock.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    # node Reroute.019
    reroute_019 = martianrock.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    # node Reroute.020
    reroute_020 = martianrock.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    # node Reroute.021
    reroute_021 = martianrock.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    # node Reroute.022
    reroute_022 = martianrock.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    # node Frame.005
    frame_005 = martianrock.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # node Math.001
    math_001_1 = martianrock.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = "ADD"
    math_001_1.use_clamp = False

    # node Integer.001
    integer_001 = martianrock.nodes.new("FunctionNodeInputInt")
    integer_001.label = "Global Seed Offset"
    integer_001.name = "Integer.001"
    integer_001.integer = 0

    # Set parents
    cube.parent = frame_002
    subdivision_surface.parent = frame_002
    set_position.parent = frame_1
    voronoi_texture.parent = frame_1
    vector_math.parent = frame_1
    position.parent = frame_1
    map_range.parent = frame_1
    set_position_001.parent = frame_001_1
    vector_math_001.parent = frame_001_1
    position_001.parent = frame_001_1
    noise_texture.parent = frame_001_1
    reroute_001.parent = frame_001_1
    transform_geometry.parent = frame_003_1
    reroute_002.parent = frame_002
    attribute_statistic.parent = frame_003_1
    position_002.parent = frame_003_1
    reroute_003.parent = frame_003_1
    vector_math_002.parent = frame_003_1
    vector_math_003.parent = frame_003_1
    vector_math_004.parent = frame_003_1
    group.parent = frame_1
    group_001.parent = frame_1
    group_002.parent = frame_1
    group_004.parent = frame_1
    float_curve.parent = frame_1
    group_005.parent = frame_1
    reroute_005.parent = frame_1
    group_003.parent = frame_002
    group_006.parent = frame_002
    reroute_006.parent = frame_002
    group_007.parent = frame_001_1
    group_008.parent = frame_001_1
    group_010.parent = frame_001_1
    group_011.parent = frame_001_1
    group_012.parent = frame_001_1
    transform_geometry_001.parent = frame_002
    random_value.parent = frame_002
    integer.parent = frame_002
    delete_geometry.parent = frame_004
    compare.parent = frame_004
    position_004.parent = frame_004
    separate_xyz_001.parent = frame_004
    normal_001.parent = frame_004
    boolean_math.parent = frame_004
    separate_xyz_002.parent = frame_004
    compare_001.parent = frame_004
    mesh_boolean.parent = frame_004
    switch_1.parent = frame_004
    transform_geometry_002.parent = frame_004
    combine_xyz.parent = frame_004
    cube_001.parent = frame_004
    math_1.parent = frame_004
    reroute_004.parent = frame_004
    reroute_012.parent = frame_004
    transform_geometry_003.parent = frame_005
    combine_xyz_001.parent = frame_005
    group_009.parent = frame_005
    group_013.parent = frame_005
    group_014.parent = frame_005
    separate_xyz.parent = frame_005
    separate_xyz_003.parent = frame_005

    # Set locations
    group_input_2.location = (-4957.7626953125, -82.99918365478516)
    group_output_2.location = (2629.999755859375, 0.0)
    set_material.location = (2439.999755859375, 23.5)
    cube.location = (-1513.1207275390625, 915.7615966796875)
    subdivision_surface.location = (-340.2048034667969, 1023.5044555664062)
    set_position.location = (726.622314453125, 908.64501953125)
    voronoi_texture.location = (-133.37771606445312, 678.8929443359375)
    vector_math.location = (536.622314453125, 703.8929443359375)
    position.location = (346.6222839355469, 666.3929443359375)
    map_range.location = (346.6222839355469, 601.3929443359375)
    set_position_001.location = (1584.2333984375, 260.2159423828125)
    vector_math_001.location = (1394.2333984375, 108.06204986572266)
    position_001.location = (1204.2333984375, 70.56206512451172)
    noise_texture.location = (1001.9918212890625, 32.7781982421875)
    set_shade_smooth.location = (2249.999755859375, 35.5)
    frame_1.location = (-2794.595703125, 186.608642578125)
    frame_001_1.location = (-3649.0771484375, -318.5823059082031)
    frame_002.location = (-3290.830078125, 71.48291015625)
    reroute_001.location = (666.5570068359375, -219.35711669921875)
    transform_geometry.location = (1809.3837890625, -34.2188835144043)
    reroute_002.location = (-688.463623046875, 896.0345458984375)
    attribute_statistic.location = (1183.53466796875, -268.6141662597656)
    position_002.location = (993.53466796875, -339.6141662597656)
    reroute_003.location = (1086.59716796875, -128.1580352783203)
    vector_math_002.location = (1373.53466796875, -337.17041015625)
    vector_math_003.location = (1373.53466796875, -197.17041015625)
    vector_math_004.location = (1563.53466796875, -198.17041015625)
    group.location = (-434.4251708984375, 622.037353515625)
    group_001.location = (-434.4251708984375, 800.037353515625)
    group_002.location = (-434.4251708984375, 422.037353515625)
    group_004.location = (-434.4251708984375, 22.037353515625)
    float_curve.location = (56.622283935546875, 636.3929443359375)
    group_005.location = (-434.4251708984375, 222.037353515625)
    reroute_005.location = (-594.6759643554688, 278.4246826171875)
    group_003.location = (-654.701904296875, 678.068603515625)
    group_006.location = (-654.701904296875, 878.068603515625)
    reroute_006.location = (-694.4317626953125, 732.759765625)
    reroute.location = (-3415.009765625, -1250.500732421875)
    group_007.location = (733.760498046875, 245.83392333984375)
    group_008.location = (733.760498046875, 67.83392333984375)
    group_010.location = (733.760498046875, -132.16607666015625)
    group_011.location = (733.760498046875, -332.16607666015625)
    group_012.location = (733.760498046875, -532.1660766601562)
    frame_003_1.location = (-2665.356201171875, 28.966693878173828)
    transform_geometry_001.location = (-943.1207275390625, 961.654052734375)
    random_value.location = (-1133.1207275390625, 838.7128295898438)
    integer.location = (-1323.1207275390625, 816.7128295898438)
    delete_geometry.location = (1346.2703857421875, -536.0291137695312)
    compare.location = (966.2703857421875, -950.8118896484375)
    position_004.location = (586.2703857421875, -1009.8118896484375)
    separate_xyz_001.location = (776.2703857421875, -997.3118896484375)
    normal_001.location = (586.2703857421875, -828.6788330078125)
    boolean_math.location = (1156.2703857421875, -769.6106567382812)
    separate_xyz_002.location = (776.2703857421875, -816.1788330078125)
    compare_001.location = (966.2703857421875, -769.6788330078125)
    mesh_boolean.location = (965.2637939453125, -511.6483154296875)
    switch_1.location = (1665.2486572265625, -268.939453125)
    transform_geometry_002.location = (775.2637939453125, -585.58447265625)
    combine_xyz.location = (585.2637939453125, -656.6286010742188)
    reroute_010.location = (-3415.009765625, -1287.8094482421875)
    cube_001.location = (395.2638244628906, -535.58447265625)
    math_1.location = (395.2638244628906, -773.58447265625)
    reroute_004.location = (702.1375732421875, -330.8438720703125)
    frame_004.location = (-904.48779296875, 272.091064453125)
    reroute_012.location = (368.2854309082031, -1095.044189453125)
    reroute_013.location = (-3415.009765625, -1303.5126953125)
    transform_geometry_003.location = (1706.2198486328125, -32.31362533569336)
    combine_xyz_001.location = (1538.015380859375, -398.0220642089844)
    group_009.location = (1308.17041015625, -245.8809814453125)
    group_013.location = (1308.17041015625, -445.8809814453125)
    group_014.location = (1308.17041015625, -645.8809814453125)
    reroute_015.location = (-3415.009765625, -1234.2786865234375)
    separate_xyz.location = (949.9049682617188, -448.3955383300781)
    separate_xyz_003.location = (949.9049682617188, -582.3955078125)
    reroute_017.location = (-3415.009765625, -1270.66552734375)
    reroute_018.location = (871.9225463867188, -1251.0347900390625)
    reroute_019.location = (871.9225463867188, -1271.1376953125)
    reroute_020.location = (1295.392578125, -1234.255126953125)
    reroute_021.location = (559.1981201171875, -1287.5440673828125)
    reroute_022.location = (-1005.0067138671875, -1303.1754150390625)
    frame_005.location = (145.8409423828125, 25.487651824951172)
    math_001_1.location = (-4690.5810546875, -4.762271881103516)
    integer_001.location = (-4956.11669921875, 50.9406852722168)

    # initialize martianrock links
    # set_material.Geometry -> group_output_2.Geometry
    martianrock.links.new(set_material.outputs[0], group_output_2.inputs[0])
    # set_shade_smooth.Geometry -> set_material.Geometry
    martianrock.links.new(set_shade_smooth.outputs[0], set_material.inputs[0])
    # reroute_002.Output -> subdivision_surface.Level
    martianrock.links.new(reroute_002.outputs[0], subdivision_surface.inputs[1])
    # position.Position -> vector_math.Vector
    martianrock.links.new(position.outputs[0], vector_math.inputs[0])
    # map_range.Result -> vector_math.Vector
    martianrock.links.new(map_range.outputs[0], vector_math.inputs[1])
    # vector_math.Vector -> set_position.Position
    martianrock.links.new(vector_math.outputs[0], set_position.inputs[2])
    # position_001.Position -> vector_math_001.Vector
    martianrock.links.new(position_001.outputs[0], vector_math_001.inputs[0])
    # noise_texture.Fac -> vector_math_001.Vector
    martianrock.links.new(noise_texture.outputs[0], vector_math_001.inputs[1])
    # reroute_003.Output -> transform_geometry.Geometry
    martianrock.links.new(reroute_003.outputs[0], transform_geometry.inputs[0])
    # math_001_1.Value -> reroute_001.Input
    martianrock.links.new(math_001_1.outputs[0], reroute_001.inputs[0])
    # position_002.Position -> attribute_statistic.Attribute
    martianrock.links.new(position_002.outputs[0], attribute_statistic.inputs[2])
    # set_position_001.Geometry -> reroute_003.Input
    martianrock.links.new(set_position_001.outputs[0], reroute_003.inputs[0])
    # reroute_003.Output -> attribute_statistic.Geometry
    martianrock.links.new(reroute_003.outputs[0], attribute_statistic.inputs[0])
    # vector_math_002.Vector -> transform_geometry.Scale
    martianrock.links.new(vector_math_002.outputs[0], transform_geometry.inputs[3])
    # attribute_statistic.Range -> vector_math_002.Vector
    martianrock.links.new(attribute_statistic.outputs[5], vector_math_002.inputs[1])
    # vector_math_004.Vector -> transform_geometry.Translation
    martianrock.links.new(vector_math_004.outputs[0], transform_geometry.inputs[1])
    # vector_math_003.Vector -> vector_math_004.Vector
    martianrock.links.new(vector_math_003.outputs[0], vector_math_004.inputs[0])
    # attribute_statistic.Min -> vector_math_003.Vector
    martianrock.links.new(attribute_statistic.outputs[3], vector_math_003.inputs[0])
    # attribute_statistic.Max -> vector_math_003.Vector
    martianrock.links.new(attribute_statistic.outputs[4], vector_math_003.inputs[1])
    # group_001.Value -> voronoi_texture.W
    martianrock.links.new(group_001.outputs[0], voronoi_texture.inputs[1])
    # reroute_005.Output -> group_001.Seed
    martianrock.links.new(reroute_005.outputs[0], group_001.inputs[2])
    # group.Value -> voronoi_texture.Scale
    martianrock.links.new(group.outputs[0], voronoi_texture.inputs[2])
    # group_002.Value -> voronoi_texture.Detail
    martianrock.links.new(group_002.outputs[0], voronoi_texture.inputs[3])
    # group_004.Value -> voronoi_texture.Lacunarity
    martianrock.links.new(group_004.outputs[0], voronoi_texture.inputs[5])
    # reroute_005.Output -> group.Seed
    martianrock.links.new(reroute_005.outputs[0], group.inputs[3])
    # reroute_005.Output -> group_002.Seed
    martianrock.links.new(reroute_005.outputs[0], group_002.inputs[3])
    # reroute_005.Output -> group_004.Seed
    martianrock.links.new(reroute_005.outputs[0], group_004.inputs[3])
    # subdivision_surface.Mesh -> set_position.Geometry
    martianrock.links.new(subdivision_surface.outputs[0], set_position.inputs[0])
    # set_position.Geometry -> set_position_001.Geometry
    martianrock.links.new(set_position.outputs[0], set_position_001.inputs[0])
    # float_curve.Value -> map_range.Value
    martianrock.links.new(float_curve.outputs[0], map_range.inputs[0])
    # voronoi_texture.Distance -> float_curve.Value
    martianrock.links.new(voronoi_texture.outputs[0], float_curve.inputs[1])
    # reroute_005.Output -> group_005.Seed
    martianrock.links.new(reroute_005.outputs[0], group_005.inputs[3])
    # group_005.Value -> voronoi_texture.Roughness
    martianrock.links.new(group_005.outputs[0], voronoi_texture.inputs[4])
    # math_001_1.Value -> reroute_005.Input
    martianrock.links.new(math_001_1.outputs[0], reroute_005.inputs[0])
    # reroute_006.Output -> group_003.Seed
    martianrock.links.new(reroute_006.outputs[0], group_003.inputs[3])
    # reroute_006.Output -> group_006.Seed
    martianrock.links.new(reroute_006.outputs[0], group_006.inputs[3])
    # group_003.Value -> subdivision_surface.Vertex Crease
    martianrock.links.new(group_003.outputs[0], subdivision_surface.inputs[3])
    # group_006.Value -> subdivision_surface.Edge Crease
    martianrock.links.new(group_006.outputs[0], subdivision_surface.inputs[2])
    # math_001_1.Value -> reroute_006.Input
    martianrock.links.new(math_001_1.outputs[0], reroute_006.inputs[0])
    # group_input_2.Scale -> reroute.Input
    martianrock.links.new(group_input_2.outputs[2], reroute.inputs[0])
    # group_input_2.Subdivisions -> reroute_002.Input
    martianrock.links.new(group_input_2.outputs[1], reroute_002.inputs[0])
    # vector_math_001.Vector -> set_position_001.Position
    martianrock.links.new(vector_math_001.outputs[0], set_position_001.inputs[2])
    # reroute_001.Output -> group_007.Seed
    martianrock.links.new(reroute_001.outputs[0], group_007.inputs[2])
    # group_007.Value -> noise_texture.W
    martianrock.links.new(group_007.outputs[0], noise_texture.inputs[1])
    # reroute_001.Output -> group_008.Seed
    martianrock.links.new(reroute_001.outputs[0], group_008.inputs[3])
    # reroute_001.Output -> group_010.Seed
    martianrock.links.new(reroute_001.outputs[0], group_010.inputs[3])
    # reroute_001.Output -> group_011.Seed
    martianrock.links.new(reroute_001.outputs[0], group_011.inputs[3])
    # reroute_001.Output -> group_012.Seed
    martianrock.links.new(reroute_001.outputs[0], group_012.inputs[3])
    # group_012.Value -> noise_texture.Distortion
    martianrock.links.new(group_012.outputs[0], noise_texture.inputs[8])
    # group_010.Value -> noise_texture.Roughness
    martianrock.links.new(group_010.outputs[0], noise_texture.inputs[4])
    # group_011.Value -> noise_texture.Lacunarity
    martianrock.links.new(group_011.outputs[0], noise_texture.inputs[5])
    # group_008.Value -> noise_texture.Scale
    martianrock.links.new(group_008.outputs[0], noise_texture.inputs[2])
    # integer.Integer -> random_value.ID
    martianrock.links.new(integer.outputs[0], random_value.inputs[7])
    # random_value.Value -> transform_geometry_001.Rotation
    martianrock.links.new(random_value.outputs[0], transform_geometry_001.inputs[2])
    # transform_geometry_001.Geometry -> subdivision_surface.Mesh
    martianrock.links.new(
        transform_geometry_001.outputs[0], subdivision_surface.inputs[0]
    )
    # cube.Mesh -> transform_geometry_001.Geometry
    martianrock.links.new(cube.outputs[0], transform_geometry_001.inputs[0])
    # math_001_1.Value -> random_value.Seed
    martianrock.links.new(math_001_1.outputs[0], random_value.inputs[8])
    # mesh_boolean.Mesh -> delete_geometry.Geometry
    martianrock.links.new(mesh_boolean.outputs[0], delete_geometry.inputs[0])
    # position_004.Position -> compare.A
    martianrock.links.new(position_004.outputs[0], compare.inputs[4])
    # separate_xyz_001.Z -> compare.A
    martianrock.links.new(separate_xyz_001.outputs[2], compare.inputs[0])
    # normal_001.Normal -> separate_xyz_002.Vector
    martianrock.links.new(normal_001.outputs[0], separate_xyz_002.inputs[0])
    # separate_xyz_002.Z -> compare_001.A
    martianrock.links.new(separate_xyz_002.outputs[2], compare_001.inputs[0])
    # boolean_math.Boolean -> delete_geometry.Selection
    martianrock.links.new(boolean_math.outputs[0], delete_geometry.inputs[1])
    # reroute_004.Output -> mesh_boolean.Mesh 1
    martianrock.links.new(reroute_004.outputs[0], mesh_boolean.inputs[0])
    # transform_geometry_002.Geometry -> mesh_boolean.Mesh 2
    martianrock.links.new(transform_geometry_002.outputs[0], mesh_boolean.inputs[1])
    # position_004.Position -> separate_xyz_001.Vector
    martianrock.links.new(position_004.outputs[0], separate_xyz_001.inputs[0])
    # reroute_021.Output -> switch_1.Switch
    martianrock.links.new(reroute_021.outputs[0], switch_1.inputs[0])
    # transform_geometry_003.Geometry -> set_shade_smooth.Geometry
    martianrock.links.new(transform_geometry_003.outputs[0], set_shade_smooth.inputs[0])
    # reroute_004.Output -> switch_1.False
    martianrock.links.new(reroute_004.outputs[0], switch_1.inputs[1])
    # delete_geometry.Geometry -> switch_1.True
    martianrock.links.new(delete_geometry.outputs[0], switch_1.inputs[2])
    # math_1.Value -> combine_xyz.Z
    martianrock.links.new(math_1.outputs[0], combine_xyz.inputs[2])
    # reroute_012.Output -> compare.B
    martianrock.links.new(reroute_012.outputs[0], compare.inputs[1])
    # group_input_2.Horizontal Cut -> reroute_010.Input
    martianrock.links.new(group_input_2.outputs[4], reroute_010.inputs[0])
    # compare_001.Result -> boolean_math.Boolean
    martianrock.links.new(compare_001.outputs[0], boolean_math.inputs[0])
    # compare.Result -> boolean_math.Boolean
    martianrock.links.new(compare.outputs[0], boolean_math.inputs[1])
    # cube_001.Mesh -> transform_geometry_002.Geometry
    martianrock.links.new(cube_001.outputs[0], transform_geometry_002.inputs[0])
    # combine_xyz.Vector -> transform_geometry_002.Translation
    martianrock.links.new(combine_xyz.outputs[0], transform_geometry_002.inputs[1])
    # reroute_012.Output -> math_1.Value
    martianrock.links.new(reroute_012.outputs[0], math_1.inputs[0])
    # transform_geometry.Geometry -> reroute_004.Input
    martianrock.links.new(transform_geometry.outputs[0], reroute_004.inputs[0])
    # reroute_022.Output -> reroute_012.Input
    martianrock.links.new(reroute_022.outputs[0], reroute_012.inputs[0])
    # group_input_2.Horizontal Cut Offset -> reroute_013.Input
    martianrock.links.new(group_input_2.outputs[5], reroute_013.inputs[0])
    # switch_1.Output -> transform_geometry_003.Geometry
    martianrock.links.new(switch_1.outputs[0], transform_geometry_003.inputs[0])
    # group_009.Value -> combine_xyz_001.X
    martianrock.links.new(group_009.outputs[0], combine_xyz_001.inputs[0])
    # group_013.Value -> combine_xyz_001.Y
    martianrock.links.new(group_013.outputs[0], combine_xyz_001.inputs[1])
    # group_014.Value -> combine_xyz_001.Z
    martianrock.links.new(group_014.outputs[0], combine_xyz_001.inputs[2])
    # combine_xyz_001.Vector -> transform_geometry_003.Scale
    martianrock.links.new(combine_xyz_001.outputs[0], transform_geometry_003.inputs[3])
    # math_001_1.Value -> reroute_015.Input
    martianrock.links.new(math_001_1.outputs[0], reroute_015.inputs[0])
    # reroute_020.Output -> group_013.Seed
    martianrock.links.new(reroute_020.outputs[0], group_013.inputs[3])
    # reroute_020.Output -> group_009.Seed
    martianrock.links.new(reroute_020.outputs[0], group_009.inputs[3])
    # reroute_020.Output -> group_014.Seed
    martianrock.links.new(reroute_020.outputs[0], group_014.inputs[3])
    # reroute_019.Output -> separate_xyz_003.Vector
    martianrock.links.new(reroute_019.outputs[0], separate_xyz_003.inputs[0])
    # separate_xyz_003.X -> group_009.Std. Dev.
    martianrock.links.new(separate_xyz_003.outputs[0], group_009.inputs[2])
    # separate_xyz_003.Y -> group_013.Std. Dev.
    martianrock.links.new(separate_xyz_003.outputs[1], group_013.inputs[2])
    # separate_xyz_003.Z -> group_014.Std. Dev.
    martianrock.links.new(separate_xyz_003.outputs[2], group_014.inputs[2])
    # separate_xyz.X -> group_009.Mean
    martianrock.links.new(separate_xyz.outputs[0], group_009.inputs[1])
    # separate_xyz.Y -> group_013.Mean
    martianrock.links.new(separate_xyz.outputs[1], group_013.inputs[1])
    # separate_xyz.Z -> group_014.Mean
    martianrock.links.new(separate_xyz.outputs[2], group_014.inputs[1])
    # reroute_018.Output -> separate_xyz.Vector
    martianrock.links.new(reroute_018.outputs[0], separate_xyz.inputs[0])
    # group_input_2.Scale STD -> reroute_017.Input
    martianrock.links.new(group_input_2.outputs[3], reroute_017.inputs[0])
    # reroute.Output -> reroute_018.Input
    martianrock.links.new(reroute.outputs[0], reroute_018.inputs[0])
    # reroute_017.Output -> reroute_019.Input
    martianrock.links.new(reroute_017.outputs[0], reroute_019.inputs[0])
    # reroute_015.Output -> reroute_020.Input
    martianrock.links.new(reroute_015.outputs[0], reroute_020.inputs[0])
    # reroute_010.Output -> reroute_021.Input
    martianrock.links.new(reroute_010.outputs[0], reroute_021.inputs[0])
    # reroute_013.Output -> reroute_022.Input
    martianrock.links.new(reroute_013.outputs[0], reroute_022.inputs[0])
    # group_input_2.Seed -> math_001_1.Value
    martianrock.links.new(group_input_2.outputs[0], math_001_1.inputs[0])
    # integer_001.Integer -> math_001_1.Value
    martianrock.links.new(integer_001.outputs[0], math_001_1.inputs[1])
    return martianrock


martianrock = martianrock_node_group()


# initialize crater_profile node group
def crater_profile_node_group():
    crater_profile = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="Crater Profile"
    )

    crater_profile.color_tag = "NONE"
    crater_profile.description = ""

    # crater_profile interface
    # Socket Value
    value_socket_2 = crater_profile.interface.new_socket(
        name="Value", in_out="OUTPUT", socket_type="NodeSocketFloat"
    )
    value_socket_2.default_value = 0.0
    value_socket_2.min_value = -3.4028234663852886e38
    value_socket_2.max_value = 3.4028234663852886e38
    value_socket_2.subtype = "NONE"
    value_socket_2.attribute_domain = "POINT"

    # Socket Value
    value_socket_3 = crater_profile.interface.new_socket(
        name="Value", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    value_socket_3.default_value = 1.0
    value_socket_3.min_value = -3.4028234663852886e38
    value_socket_3.max_value = 3.4028234663852886e38
    value_socket_3.subtype = "NONE"
    value_socket_3.attribute_domain = "POINT"

    # Socket Crater Radius Fraction
    crater_radius_fraction_socket = crater_profile.interface.new_socket(
        name="Crater Radius Fraction", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    crater_radius_fraction_socket.default_value = 0.0
    crater_radius_fraction_socket.min_value = 1.0
    crater_radius_fraction_socket.max_value = 3.4028234663852886e38
    crater_radius_fraction_socket.subtype = "FACTOR"
    crater_radius_fraction_socket.attribute_domain = "POINT"

    # Socket Max Crater Radius
    max_crater_radius_socket = crater_profile.interface.new_socket(
        name="Max Crater Radius", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    max_crater_radius_socket.default_value = 0.0
    max_crater_radius_socket.min_value = -3.4028234663852886e38
    max_crater_radius_socket.max_value = 3.4028234663852886e38
    max_crater_radius_socket.subtype = "NONE"
    max_crater_radius_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_3 = crater_profile.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket_3.default_value = 0
    seed_socket_3.min_value = 0
    seed_socket_3.max_value = 2147483647
    seed_socket_3.subtype = "NONE"
    seed_socket_3.attribute_domain = "POINT"
    seed_socket_3.force_non_field = True

    # initialize crater_profile nodes
    # node Group Output
    group_output_3 = crater_profile.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True

    # node Group Input
    group_input_3 = crater_profile.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"

    # node Noise Texture.011
    noise_texture_011 = crater_profile.nodes.new("ShaderNodeTexNoise")
    noise_texture_011.name = "Noise Texture.011"
    noise_texture_011.noise_dimensions = "4D"
    noise_texture_011.noise_type = "FBM"
    noise_texture_011.normalize = True
    # Vector
    noise_texture_011.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Detail
    noise_texture_011.inputs[3].default_value = 15.0
    # Distortion
    noise_texture_011.inputs[8].default_value = 0.0

    # node Group.019
    group_019 = crater_profile.nodes.new("GeometryNodeGroup")
    group_019.name = "Group.019"
    group_019.node_tree = random__uniform_
    # Socket_1
    group_019.inputs[0].default_value = -100000000.0
    # Socket_2
    group_019.inputs[1].default_value = 1000000000.0
    # Socket_4
    group_019.inputs[3].default_value = 46364

    # node Group.022
    group_022 = crater_profile.nodes.new("GeometryNodeGroup")
    group_022.name = "Group.022"
    group_022.node_tree = random__normal_
    # Socket_1
    group_022.inputs[0].default_value = False
    # Socket_5
    group_022.inputs[4].default_value = 2808

    # node Group.023
    group_023 = crater_profile.nodes.new("GeometryNodeGroup")
    group_023.name = "Group.023"
    group_023.node_tree = random__normal_
    # Socket_1
    group_023.inputs[0].default_value = True
    # Socket_2
    group_023.inputs[1].default_value = 0.30000001192092896
    # Socket_3
    group_023.inputs[2].default_value = 0.02500000037252903
    # Socket_5
    group_023.inputs[4].default_value = 8508

    # node Group.024
    group_024 = crater_profile.nodes.new("GeometryNodeGroup")
    group_024.name = "Group.024"
    group_024.node_tree = random__normal_
    # Socket_1
    group_024.inputs[0].default_value = True
    # Socket_2
    group_024.inputs[1].default_value = 2.25
    # Socket_3
    group_024.inputs[2].default_value = 0.25
    # Socket_5
    group_024.inputs[4].default_value = 141

    # node Float to Integer
    float_to_integer = crater_profile.nodes.new("FunctionNodeFloatToInt")
    float_to_integer.name = "Float to Integer"
    float_to_integer.rounding_mode = "ROUND"

    # node Math.001
    math_001_2 = crater_profile.nodes.new("ShaderNodeMath")
    math_001_2.label = "Metric radius"
    math_001_2.name = "Math.001"
    math_001_2.operation = "MULTIPLY"
    math_001_2.use_clamp = False
    math_001_2.inputs[2].hide = True

    # node Reroute.002
    reroute_002_1 = crater_profile.nodes.new("NodeReroute")
    reroute_002_1.name = "Reroute.002"
    # node Integer
    integer_1 = crater_profile.nodes.new("FunctionNodeInputInt")
    integer_1.label = "Max N"
    integer_1.name = "Integer"
    integer_1.integer = 4

    # node Math.003
    math_003_1 = crater_profile.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = "ADD"
    math_003_1.use_clamp = False

    # node Map Range
    map_range_1 = crater_profile.nodes.new("ShaderNodeMapRange")
    map_range_1.name = "Map Range"
    map_range_1.clamp = True
    map_range_1.data_type = "FLOAT"
    map_range_1.interpolation_type = "LINEAR"
    # From Min
    map_range_1.inputs[1].default_value = 0.0
    # From Max
    map_range_1.inputs[2].default_value = 1.0
    # To Min
    map_range_1.inputs[3].default_value = 0.0

    # node Group
    group_1 = crater_profile.nodes.new("GeometryNodeGroup")
    group_1.name = "Group"
    group_1.node_tree = random__normal_
    # Socket_1
    group_1.inputs[0].default_value = True
    # Socket_2
    group_1.inputs[1].default_value = 0.0
    # Socket_3
    group_1.inputs[2].default_value = 0.25
    # Socket_5
    group_1.inputs[4].default_value = 24183

    # node Float Curve.004
    float_curve_004 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_004.name = "Float Curve.004"
    # mapping settings
    float_curve_004.mapping.extend = "EXTRAPOLATED"
    float_curve_004.mapping.tone = "STANDARD"
    float_curve_004.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_004.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_004.mapping.clip_min_x = 0.0
    float_curve_004.mapping.clip_min_y = 0.0
    float_curve_004.mapping.clip_max_x = 1.0
    float_curve_004.mapping.clip_max_y = 1.0
    float_curve_004.mapping.use_clip = True
    # curve 0
    float_curve_004_curve_0 = float_curve_004.mapping.curves[0]
    float_curve_004_curve_0_point_0 = float_curve_004_curve_0.points[0]
    float_curve_004_curve_0_point_0.location = (0.0, 0.6302875280380249)
    float_curve_004_curve_0_point_0.handle_type = "AUTO"
    float_curve_004_curve_0_point_1 = float_curve_004_curve_0.points[1]
    float_curve_004_curve_0_point_1.location = (0.20408575236797333, 0.6508127450942993)
    float_curve_004_curve_0_point_1.handle_type = "AUTO"
    float_curve_004_curve_0_point_2 = float_curve_004_curve_0.points.new(
        0.3318162262439728, 0.7192298769950867
    )
    float_curve_004_curve_0_point_2.handle_type = "AUTO"
    float_curve_004_curve_0_point_3 = float_curve_004_curve_0.points.new(
        0.4255254566669464, 0.7699005007743835
    )
    float_curve_004_curve_0_point_3.handle_type = "AUTO"
    float_curve_004_curve_0_point_4 = float_curve_004_curve_0.points.new(
        0.5083944797515869, 0.5437449216842651
    )
    float_curve_004_curve_0_point_4.handle_type = "AUTO"
    float_curve_004_curve_0_point_5 = float_curve_004_curve_0.points.new(
        0.7643035054206848, 0.13317757844924927
    )
    float_curve_004_curve_0_point_5.handle_type = "AUTO"
    float_curve_004_curve_0_point_6 = float_curve_004_curve_0.points.new(
        1.0, 0.056249916553497314
    )
    float_curve_004_curve_0_point_6.handle_type = "AUTO"
    # update curve after changes
    float_curve_004.mapping.update()
    # Factor
    float_curve_004.inputs[0].default_value = 1.0

    # node Float Curve.005
    float_curve_005 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_005.name = "Float Curve.005"
    # mapping settings
    float_curve_005.mapping.extend = "EXTRAPOLATED"
    float_curve_005.mapping.tone = "STANDARD"
    float_curve_005.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_005.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_005.mapping.clip_min_x = 0.0
    float_curve_005.mapping.clip_min_y = 0.0
    float_curve_005.mapping.clip_max_x = 1.0
    float_curve_005.mapping.clip_max_y = 1.0
    float_curve_005.mapping.use_clip = True
    # curve 0
    float_curve_005_curve_0 = float_curve_005.mapping.curves[0]
    float_curve_005_curve_0_point_0 = float_curve_005_curve_0.points[0]
    float_curve_005_curve_0_point_0.location = (0.0, 0.6241841912269592)
    float_curve_005_curve_0_point_0.handle_type = "AUTO"
    float_curve_005_curve_0_point_1 = float_curve_005_curve_0.points[1]
    float_curve_005_curve_0_point_1.location = (0.20329293608665466, 0.6318109631538391)
    float_curve_005_curve_0_point_1.handle_type = "AUTO"
    float_curve_005_curve_0_point_2 = float_curve_005_curve_0.points.new(
        0.3409092426300049, 0.6676813960075378
    )
    float_curve_005_curve_0_point_2.handle_type = "AUTO_CLAMPED"
    float_curve_005_curve_0_point_3 = float_curve_005_curve_0.points.new(
        0.5181822776794434, 0.4260922968387604
    )
    float_curve_005_curve_0_point_3.handle_type = "AUTO"
    float_curve_005_curve_0_point_4 = float_curve_005_curve_0.points.new(
        0.7181820273399353, 0.2250000238418579
    )
    float_curve_005_curve_0_point_4.handle_type = "AUTO"
    float_curve_005_curve_0_point_5 = float_curve_005_curve_0.points.new(
        1.0, 0.16875003278255463
    )
    float_curve_005_curve_0_point_5.handle_type = "AUTO"
    # update curve after changes
    float_curve_005.mapping.update()
    # Factor
    float_curve_005.inputs[0].default_value = 1.0

    # node Float Curve.006
    float_curve_006 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_006.name = "Float Curve.006"
    # mapping settings
    float_curve_006.mapping.extend = "EXTRAPOLATED"
    float_curve_006.mapping.tone = "STANDARD"
    float_curve_006.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_006.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_006.mapping.clip_min_x = 0.0
    float_curve_006.mapping.clip_min_y = 0.0
    float_curve_006.mapping.clip_max_x = 1.0
    float_curve_006.mapping.clip_max_y = 1.0
    float_curve_006.mapping.use_clip = True
    # curve 0
    float_curve_006_curve_0 = float_curve_006.mapping.curves[0]
    float_curve_006_curve_0_point_0 = float_curve_006_curve_0.points[0]
    float_curve_006_curve_0_point_0.location = (0.0, 0.6725000739097595)
    float_curve_006_curve_0_point_0.handle_type = "AUTO"
    float_curve_006_curve_0_point_1 = float_curve_006_curve_0.points[1]
    float_curve_006_curve_0_point_1.location = (0.18717996776103973, 0.6866194605827332)
    float_curve_006_curve_0_point_1.handle_type = "AUTO"
    float_curve_006_curve_0_point_2 = float_curve_006_curve_0.points.new(
        0.38181814551353455, 0.7312501072883606
    )
    float_curve_006_curve_0_point_2.handle_type = "AUTO"
    float_curve_006_curve_0_point_3 = float_curve_006_curve_0.points.new(
        0.47272729873657227, 0.7426979541778564
    )
    float_curve_006_curve_0_point_3.handle_type = "AUTO"
    float_curve_006_curve_0_point_4 = float_curve_006_curve_0.points.new(
        0.6454547047615051, 0.24985311925411224
    )
    float_curve_006_curve_0_point_4.handle_type = "AUTO"
    float_curve_006_curve_0_point_5 = float_curve_006_curve_0.points.new(
        1.0, 0.13730427622795105
    )
    float_curve_006_curve_0_point_5.handle_type = "AUTO"
    # update curve after changes
    float_curve_006.mapping.update()
    # Factor
    float_curve_006.inputs[0].default_value = 1.0

    # node Float Curve.007
    float_curve_007 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_007.name = "Float Curve.007"
    # mapping settings
    float_curve_007.mapping.extend = "EXTRAPOLATED"
    float_curve_007.mapping.tone = "STANDARD"
    float_curve_007.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_007.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_007.mapping.clip_min_x = 0.0
    float_curve_007.mapping.clip_min_y = 0.0
    float_curve_007.mapping.clip_max_x = 1.0
    float_curve_007.mapping.clip_max_y = 1.0
    float_curve_007.mapping.use_clip = True
    # curve 0
    float_curve_007_curve_0 = float_curve_007.mapping.curves[0]
    float_curve_007_curve_0_point_0 = float_curve_007_curve_0.points[0]
    float_curve_007_curve_0_point_0.location = (0.0, 0.7124999761581421)
    float_curve_007_curve_0_point_0.handle_type = "AUTO"
    float_curve_007_curve_0_point_1 = float_curve_007_curve_0.points[1]
    float_curve_007_curve_0_point_1.location = (0.2611362040042877, 0.7326563000679016)
    float_curve_007_curve_0_point_1.handle_type = "AUTO"
    float_curve_007_curve_0_point_2 = float_curve_007_curve_0.points.new(
        0.4363635778427124, 0.7750000953674316
    )
    float_curve_007_curve_0_point_2.handle_type = "AUTO"
    float_curve_007_curve_0_point_3 = float_curve_007_curve_0.points.new(
        0.5954543352127075, 0.8114726543426514
    )
    float_curve_007_curve_0_point_3.handle_type = "AUTO"
    float_curve_007_curve_0_point_4 = float_curve_007_curve_0.points.new(
        0.6954542994499207, 0.5309724807739258
    )
    float_curve_007_curve_0_point_4.handle_type = "AUTO"
    float_curve_007_curve_0_point_5 = float_curve_007_curve_0.points.new(
        0.8590908646583557, 0.2937498986721039
    )
    float_curve_007_curve_0_point_5.handle_type = "AUTO"
    float_curve_007_curve_0_point_6 = float_curve_007_curve_0.points.new(
        1.0, 0.24999989569187164
    )
    float_curve_007_curve_0_point_6.handle_type = "AUTO"
    # update curve after changes
    float_curve_007.mapping.update()
    # Factor
    float_curve_007.inputs[0].default_value = 1.0

    # node Reroute.003
    reroute_003_1 = crater_profile.nodes.new("NodeReroute")
    reroute_003_1.name = "Reroute.003"
    # node Math.005
    math_005_1 = crater_profile.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = "MULTIPLY"
    math_005_1.use_clamp = False

    # node Index Switch.001
    index_switch_001 = crater_profile.nodes.new("GeometryNodeIndexSwitch")
    index_switch_001.name = "Index Switch.001"
    index_switch_001.data_type = "FLOAT"
    index_switch_001.index_switch_items.clear()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()

    # node Math
    math_2 = crater_profile.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = "MULTIPLY"
    math_2.use_clamp = False
    # Value_001
    math_2.inputs[1].default_value = 1.25

    # node Math.002
    math_002_1 = crater_profile.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = "MULTIPLY"
    math_002_1.use_clamp = False
    # Value_001
    math_002_1.inputs[1].default_value = 0.019999999552965164

    # node Float Curve.008
    float_curve_008 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_008.name = "Float Curve.008"
    # mapping settings
    float_curve_008.mapping.extend = "EXTRAPOLATED"
    float_curve_008.mapping.tone = "STANDARD"
    float_curve_008.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_008.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_008.mapping.clip_min_x = 0.0
    float_curve_008.mapping.clip_min_y = 0.0
    float_curve_008.mapping.clip_max_x = 1.0
    float_curve_008.mapping.clip_max_y = 1.0
    float_curve_008.mapping.use_clip = True
    # curve 0
    float_curve_008_curve_0 = float_curve_008.mapping.curves[0]
    float_curve_008_curve_0_point_0 = float_curve_008_curve_0.points[0]
    float_curve_008_curve_0_point_0.location = (0.0, 0.6662500500679016)
    float_curve_008_curve_0_point_0.handle_type = "AUTO"
    float_curve_008_curve_0_point_1 = float_curve_008_curve_0.points[1]
    float_curve_008_curve_0_point_1.location = (0.1954544186592102, 0.672716498374939)
    float_curve_008_curve_0_point_1.handle_type = "AUTO"
    float_curve_008_curve_0_point_2 = float_curve_008_curve_0.points.new(
        0.38636353611946106, 0.7116192579269409
    )
    float_curve_008_curve_0_point_2.handle_type = "AUTO"
    float_curve_008_curve_0_point_3 = float_curve_008_curve_0.points.new(
        0.7363638877868652, 0.3500000238418579
    )
    float_curve_008_curve_0_point_3.handle_type = "AUTO"
    float_curve_008_curve_0_point_4 = float_curve_008_curve_0.points.new(
        1.0, 0.29374992847442627
    )
    float_curve_008_curve_0_point_4.handle_type = "AUTO"
    # update curve after changes
    float_curve_008.mapping.update()
    # Factor
    float_curve_008.inputs[0].default_value = 1.0

    # node Math.004
    math_004_1 = crater_profile.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.operation = "INVERSE_SQRT"
    math_004_1.use_clamp = False

    # Set locations
    group_output_3.location = (712.6826171875, 17.99111557006836)
    group_input_3.location = (-3242.14990234375, -6.254646301269531)
    noise_texture_011.location = (-512.7152709960938, -439.41162109375)
    group_019.location = (-767.8524780273438, -273.099609375)
    group_022.location = (-767.8524780273438, -451.099609375)
    group_023.location = (-767.8524780273438, -651.0993041992188)
    group_024.location = (-767.8524780273438, -851.0995483398438)
    float_to_integer.location = (-1804.8189697265625, -236.50123596191406)
    math_001_2.location = (-1546.259033203125, 83.0434799194336)
    reroute_002_1.location = (-996.7823486328125, -703.491455078125)
    integer_1.location = (-1547.5233154296875, -86.2983169555664)
    math_003_1.location = (-2346.594970703125, -119.19635772705078)
    map_range_1.location = (-2156.594970703125, -72.69635772705078)
    group_1.location = (-2596.355712890625, -310.373046875)
    float_curve_004.location = (-2345.31396484375, -817.3238525390625)
    float_curve_005.location = (-2345.31396484375, -1143.3238525390625)
    float_curve_006.location = (-2345.31396484375, -1469.3238525390625)
    float_curve_007.location = (-2345.31396484375, -491.3238525390625)
    reroute_003_1.location = (-2886.522216796875, -372.5995788574219)
    math_005_1.location = (-205.45945739746094, -92.80597686767578)
    index_switch_001.location = (-1547.0994873046875, -216.50979614257812)
    math_2.location = (-1226.86962890625, -299.31927490234375)
    math_002_1.location = (-1226.86962890625, -455.403564453125)
    float_curve_008.location = (-2345.31396484375, -1795.3238525390625)
    math_004_1.location = (-1004.6797485351562, -321.485595703125)

    # initialize crater_profile links
    # group_019.Value -> noise_texture_011.W
    crater_profile.links.new(group_019.outputs[0], noise_texture_011.inputs[1])
    # reroute_002_1.Output -> group_019.Seed
    crater_profile.links.new(reroute_002_1.outputs[0], group_019.inputs[2])
    # reroute_002_1.Output -> group_022.Seed
    crater_profile.links.new(reroute_002_1.outputs[0], group_022.inputs[3])
    # reroute_002_1.Output -> group_023.Seed
    crater_profile.links.new(reroute_002_1.outputs[0], group_023.inputs[3])
    # reroute_002_1.Output -> group_024.Seed
    crater_profile.links.new(reroute_002_1.outputs[0], group_024.inputs[3])
    # group_input_3.Crater Radius Fraction -> math_001_2.Value
    crater_profile.links.new(group_input_3.outputs[1], math_001_2.inputs[0])
    # group_input_3.Max Crater Radius -> math_001_2.Value
    crater_profile.links.new(group_input_3.outputs[2], math_001_2.inputs[1])
    # math_005_1.Value -> group_output_3.Value
    crater_profile.links.new(math_005_1.outputs[0], group_output_3.inputs[0])
    # group_input_3.Seed -> reroute_002_1.Input
    crater_profile.links.new(group_input_3.outputs[3], reroute_002_1.inputs[0])
    # integer_1.Integer -> map_range_1.To Max
    crater_profile.links.new(integer_1.outputs[0], map_range_1.inputs[4])
    # map_range_1.Result -> float_to_integer.Float
    crater_profile.links.new(map_range_1.outputs[0], float_to_integer.inputs[0])
    # group_input_3.Seed -> group_1.Seed
    crater_profile.links.new(group_input_3.outputs[3], group_1.inputs[3])
    # group_1.Value -> math_003_1.Value
    crater_profile.links.new(group_1.outputs[0], math_003_1.inputs[1])
    # math_003_1.Value -> map_range_1.Value
    crater_profile.links.new(math_003_1.outputs[0], map_range_1.inputs[0])
    # group_input_3.Crater Radius Fraction -> math_003_1.Value
    crater_profile.links.new(group_input_3.outputs[1], math_003_1.inputs[0])
    # group_022.Value -> noise_texture_011.Scale
    crater_profile.links.new(group_022.outputs[0], noise_texture_011.inputs[2])
    # group_023.Value -> noise_texture_011.Roughness
    crater_profile.links.new(group_023.outputs[0], noise_texture_011.inputs[4])
    # group_024.Value -> noise_texture_011.Lacunarity
    crater_profile.links.new(group_024.outputs[0], noise_texture_011.inputs[5])
    # reroute_003_1.Output -> float_curve_004.Value
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_004.inputs[1])
    # reroute_003_1.Output -> float_curve_005.Value
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_005.inputs[1])
    # reroute_003_1.Output -> float_curve_006.Value
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_006.inputs[1])
    # reroute_003_1.Output -> float_curve_007.Value
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_007.inputs[1])
    # group_input_3.Value -> reroute_003_1.Input
    crater_profile.links.new(group_input_3.outputs[0], reroute_003_1.inputs[0])
    # noise_texture_011.Fac -> math_005_1.Value
    crater_profile.links.new(noise_texture_011.outputs[0], math_005_1.inputs[1])
    # float_curve_007.Value -> index_switch_001.0
    crater_profile.links.new(float_curve_007.outputs[0], index_switch_001.inputs[1])
    # float_curve_004.Value -> index_switch_001.1
    crater_profile.links.new(float_curve_004.outputs[0], index_switch_001.inputs[2])
    # float_curve_005.Value -> index_switch_001.2
    crater_profile.links.new(float_curve_005.outputs[0], index_switch_001.inputs[3])
    # float_curve_006.Value -> index_switch_001.3
    crater_profile.links.new(float_curve_006.outputs[0], index_switch_001.inputs[4])
    # index_switch_001.Output -> math_005_1.Value
    crater_profile.links.new(index_switch_001.outputs[0], math_005_1.inputs[0])
    # math_004_1.Value -> group_022.Mean
    crater_profile.links.new(math_004_1.outputs[0], group_022.inputs[1])
    # math_001_2.Value -> math_2.Value
    crater_profile.links.new(math_001_2.outputs[0], math_2.inputs[0])
    # math_2.Value -> math_002_1.Value
    crater_profile.links.new(math_2.outputs[0], math_002_1.inputs[0])
    # math_002_1.Value -> group_022.Std. Dev.
    crater_profile.links.new(math_002_1.outputs[0], group_022.inputs[2])
    # reroute_003_1.Output -> float_curve_008.Value
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_008.inputs[1])
    # float_curve_008.Value -> index_switch_001.4
    crater_profile.links.new(float_curve_008.outputs[0], index_switch_001.inputs[5])
    # float_to_integer.Integer -> index_switch_001.Index
    crater_profile.links.new(float_to_integer.outputs[0], index_switch_001.inputs[0])
    # math_2.Value -> math_004_1.Value
    crater_profile.links.new(math_2.outputs[0], math_004_1.inputs[0])
    return crater_profile


crater_profile = crater_profile_node_group()


# initialize martianterrain node group
def martianterrain_node_group():
    martianterrain = bpy.data.node_groups.new(
        type="GeometryNodeTree", name="MartianTerrain"
    )

    martianterrain.color_tag = "NONE"
    martianterrain.description = ""

    martianterrain.is_modifier = True

    # martianterrain interface
    # Socket Geometry
    geometry_socket_1 = martianterrain.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket_1.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_4 = martianterrain.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket_4.default_value = 0
    seed_socket_4.min_value = 0
    seed_socket_4.max_value = 2147483647
    seed_socket_4.subtype = "NONE"
    seed_socket_4.attribute_domain = "POINT"
    seed_socket_4.force_non_field = True

    # Socket Scale
    scale_socket_1 = martianterrain.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketVector"
    )
    scale_socket_1.default_value = (10.0, 10.0, 1.0)
    scale_socket_1.min_value = 0.0
    scale_socket_1.max_value = 3.4028234663852886e38
    scale_socket_1.subtype = "XYZ"
    scale_socket_1.attribute_domain = "POINT"
    scale_socket_1.force_non_field = True

    # Socket Density
    density_socket = martianterrain.interface.new_socket(
        name="Density", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    density_socket.default_value = 0.10000000149011612
    density_socket.min_value = 0.009999999776482582
    density_socket.max_value = 3.4028234663852886e38
    density_socket.subtype = "NONE"
    density_socket.attribute_domain = "POINT"
    density_socket.force_non_field = True

    # Socket Flat Area Size
    flat_area_size_socket = martianterrain.interface.new_socket(
        name="Flat Area Size", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    flat_area_size_socket.default_value = 0.0
    flat_area_size_socket.min_value = 0.0
    flat_area_size_socket.max_value = 3.4028234663852886e38
    flat_area_size_socket.subtype = "NONE"
    flat_area_size_socket.attribute_domain = "POINT"

    # Socket Rock Mesh Boolean
    rock_mesh_boolean_socket = martianterrain.interface.new_socket(
        name="Rock Mesh Boolean", in_out="INPUT", socket_type="NodeSocketBool"
    )
    rock_mesh_boolean_socket.default_value = False
    rock_mesh_boolean_socket.attribute_domain = "POINT"
    rock_mesh_boolean_socket.force_non_field = True
    rock_mesh_boolean_socket.description = "Note: Slow"

    # initialize martianterrain nodes
    # node Group Input
    group_input_4 = martianterrain.nodes.new("NodeGroupInput")
    group_input_4.name = "Group Input"

    # node Group Output
    group_output_4 = martianterrain.nodes.new("NodeGroupOutput")
    group_output_4.name = "Group Output"
    group_output_4.is_active_output = True

    # node Grid
    grid = martianterrain.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"

    # node Set Material
    set_material_1 = martianterrain.nodes.new("GeometryNodeSetMaterial")
    set_material_1.name = "Set Material"
    # Selection
    set_material_1.inputs[1].default_value = True
    if "MartianSurface" in bpy.data.materials:
        set_material_1.inputs[2].default_value = bpy.data.materials["MartianSurface"]

    # node Set Shade Smooth
    set_shade_smooth_1 = martianterrain.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_1.name = "Set Shade Smooth"
    set_shade_smooth_1.domain = "FACE"
    # Selection
    set_shade_smooth_1.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth_1.inputs[2].default_value = True

    # node Vector Math.012
    vector_math_012 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_012.name = "Vector Math.012"
    vector_math_012.operation = "SCALE"
    # Scale
    vector_math_012.inputs[3].default_value = -1.0

    # node Raycast
    raycast = martianterrain.nodes.new("GeometryNodeRaycast")
    raycast.name = "Raycast"
    raycast.data_type = "FLOAT"
    raycast.mapping = "NEAREST"
    # Attribute
    raycast.inputs[1].default_value = 0.0
    # Ray Direction
    raycast.inputs[3].default_value = (0.0, 0.0, -1.0)
    # Ray Length
    raycast.inputs[4].default_value = 10.0

    # node Frame.002
    frame_002_1 = martianterrain.nodes.new("NodeFrame")
    frame_002_1.label = "Place origin at centre"
    frame_002_1.name = "Frame.002"
    frame_002_1.label_size = 20
    frame_002_1.shrink = True

    # node Vector Math.017
    vector_math_017 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_017.name = "Vector Math.017"
    vector_math_017.operation = "MULTIPLY"

    # node Gradient Texture.001
    gradient_texture_001 = martianterrain.nodes.new("ShaderNodeTexGradient")
    gradient_texture_001.name = "Gradient Texture.001"
    gradient_texture_001.gradient_type = "QUADRATIC_SPHERE"

    # node Position.002
    position_002_1 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_002_1.name = "Position.002"

    # node Vector Math.019
    vector_math_019 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_019.name = "Vector Math.019"
    vector_math_019.operation = "DIVIDE"

    # node Set Position.001
    set_position_001_1 = martianterrain.nodes.new("GeometryNodeSetPosition")
    set_position_001_1.name = "Set Position.001"
    # Offset
    set_position_001_1.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Position.003
    position_003 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"

    # node Combine XYZ
    combine_xyz_1 = martianterrain.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_1.name = "Combine XYZ"
    # X
    combine_xyz_1.inputs[0].default_value = 1.0
    # Y
    combine_xyz_1.inputs[1].default_value = 1.0

    # node Math
    math_3 = martianterrain.nodes.new("ShaderNodeMath")
    math_3.name = "Math"
    math_3.operation = "MULTIPLY"
    math_3.use_clamp = False
    # Value_001
    math_3.inputs[1].default_value = 1.0

    # node Frame
    frame_2 = martianterrain.nodes.new("NodeFrame")
    frame_2.label = "Flatten centre"
    frame_2.name = "Frame"
    frame_2.label_size = 20
    frame_2.shrink = True

    # node Reroute.001
    reroute_001_1 = martianterrain.nodes.new("NodeReroute")
    reroute_001_1.name = "Reroute.001"
    # node Vector Math.002
    vector_math_002_1 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_002_1.name = "Vector Math.002"
    vector_math_002_1.operation = "DIVIDE"

    # node Vector Math.021
    vector_math_021 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_021.name = "Vector Math.021"
    vector_math_021.operation = "CEIL"

    # node Separate XYZ
    separate_xyz_1 = martianterrain.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_1.name = "Separate XYZ"
    separate_xyz_1.outputs[2].hide = True

    # node Vector Math.023
    vector_math_023 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_023.name = "Vector Math.023"
    vector_math_023.operation = "MAXIMUM"
    # Vector_001
    vector_math_023.inputs[1].default_value = (2.0, 2.0, 0.0)

    # node Frame.001
    frame_001_2 = martianterrain.nodes.new("NodeFrame")
    frame_001_2.label = "Base geometry"
    frame_001_2.name = "Frame.001"
    frame_001_2.label_size = 20
    frame_001_2.shrink = True

    # node Reroute.003
    reroute_003_2 = martianterrain.nodes.new("NodeReroute")
    reroute_003_2.name = "Reroute.003"
    # node Compare
    compare_1 = martianterrain.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.data_type = "FLOAT"
    compare_1.mode = "ELEMENT"
    compare_1.operation = "NOT_EQUAL"
    # B
    compare_1.inputs[1].default_value = 0.0
    # Epsilon
    compare_1.inputs[12].default_value = 0.0010000000474974513

    # node Math.001
    math_001_3 = martianterrain.nodes.new("ShaderNodeMath")
    math_001_3.name = "Math.001"
    math_001_3.operation = "ADD"
    math_001_3.use_clamp = False
    math_001_3.inputs[2].hide = True

    # node Integer.012
    integer_012 = martianterrain.nodes.new("FunctionNodeInputInt")
    integer_012.label = "Global Seed Offset"
    integer_012.name = "Integer.012"
    integer_012.integer = 0

    # node Reroute.005
    reroute_005_1 = martianterrain.nodes.new("NodeReroute")
    reroute_005_1.name = "Reroute.005"
    # node Float to Integer
    float_to_integer_1 = martianterrain.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_1.name = "Float to Integer"
    float_to_integer_1.rounding_mode = "FLOOR"

    # node Transform Geometry.001
    transform_geometry_001_1 = martianterrain.nodes.new("GeometryNodeTransform")
    transform_geometry_001_1.name = "Transform Geometry.001"
    transform_geometry_001_1.mode = "COMPONENTS"
    transform_geometry_001_1.inputs[1].hide = True
    transform_geometry_001_1.inputs[2].hide = True
    transform_geometry_001_1.inputs[4].hide = True
    # Translation
    transform_geometry_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Attribute Statistic.001
    attribute_statistic_001 = martianterrain.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_001.name = "Attribute Statistic.001"
    attribute_statistic_001.data_type = "FLOAT_VECTOR"
    attribute_statistic_001.domain = "POINT"
    attribute_statistic_001.inputs[1].hide = True
    attribute_statistic_001.outputs[0].hide = True
    attribute_statistic_001.outputs[1].hide = True
    attribute_statistic_001.outputs[2].hide = True
    attribute_statistic_001.outputs[3].hide = True
    attribute_statistic_001.outputs[4].hide = True
    attribute_statistic_001.outputs[6].hide = True
    attribute_statistic_001.outputs[7].hide = True
    # Selection
    attribute_statistic_001.inputs[1].default_value = True

    # node Position.004
    position_004_1 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_004_1.name = "Position.004"

    # node Reroute.007
    reroute_007 = martianterrain.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    # node Vector Math.028
    vector_math_028 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_028.name = "Vector Math.028"
    vector_math_028.operation = "DIVIDE"

    # node Frame.003
    frame_003_2 = martianterrain.nodes.new("NodeFrame")
    frame_003_2.label = "Final scale"
    frame_003_2.name = "Frame.003"
    frame_003_2.label_size = 20
    frame_003_2.shrink = True

    # node Reroute.008
    reroute_008 = martianterrain.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    # node Reroute.006
    reroute_006_1 = martianterrain.nodes.new("NodeReroute")
    reroute_006_1.name = "Reroute.006"
    # node Reroute.004
    reroute_004_1 = martianterrain.nodes.new("NodeReroute")
    reroute_004_1.name = "Reroute.004"
    # node Noise Texture.009
    noise_texture_009 = martianterrain.nodes.new("ShaderNodeTexNoise")
    noise_texture_009.name = "Noise Texture.009"
    noise_texture_009.noise_dimensions = "4D"
    noise_texture_009.noise_type = "MULTIFRACTAL"
    noise_texture_009.normalize = True
    # Vector
    noise_texture_009.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Distortion
    noise_texture_009.inputs[8].default_value = 0.0

    # node Group.013
    group_013_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_013_1.name = "Group.013"
    group_013_1.node_tree = random__uniform_
    # Socket_1
    group_013_1.inputs[0].default_value = -100000000.0
    # Socket_2
    group_013_1.inputs[1].default_value = 1000000000.0
    # Socket_4
    group_013_1.inputs[3].default_value = 90878

    # node Reroute.009
    reroute_009 = martianterrain.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    # node Group
    group_2 = martianterrain.nodes.new("GeometryNodeGroup")
    group_2.name = "Group"
    group_2.node_tree = random__normal_
    # Socket_1
    group_2.inputs[0].default_value = True
    # Socket_2
    group_2.inputs[1].default_value = 0.15000000596046448
    # Socket_3
    group_2.inputs[2].default_value = 0.02500000037252903
    # Socket_5
    group_2.inputs[4].default_value = 53330

    # node Group.014
    group_014_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_014_1.name = "Group.014"
    group_014_1.node_tree = random__normal_
    # Socket_1
    group_014_1.inputs[0].default_value = True
    # Socket_2
    group_014_1.inputs[1].default_value = 4.0
    # Socket_3
    group_014_1.inputs[2].default_value = 0.20000000298023224
    # Socket_5
    group_014_1.inputs[4].default_value = 48802

    # node Group.015
    group_015 = martianterrain.nodes.new("GeometryNodeGroup")
    group_015.name = "Group.015"
    group_015.node_tree = random__normal_
    # Socket_1
    group_015.inputs[0].default_value = True
    # Socket_2
    group_015.inputs[1].default_value = 0.699999988079071
    # Socket_3
    group_015.inputs[2].default_value = 0.10000000149011612
    # Socket_5
    group_015.inputs[4].default_value = 99201

    # node Group.016
    group_016 = martianterrain.nodes.new("GeometryNodeGroup")
    group_016.name = "Group.016"
    group_016.node_tree = random__normal_
    # Socket_1
    group_016.inputs[0].default_value = True
    # Socket_2
    group_016.inputs[1].default_value = 2.200000047683716
    # Socket_3
    group_016.inputs[2].default_value = 0.07500000298023224
    # Socket_5
    group_016.inputs[4].default_value = 6506

    # node Frame.004
    frame_004_1 = martianterrain.nodes.new("NodeFrame")
    frame_004_1.name = "Frame.004"
    frame_004_1.label_size = 20
    frame_004_1.shrink = True

    # node Noise Texture.010
    noise_texture_010 = martianterrain.nodes.new("ShaderNodeTexNoise")
    noise_texture_010.name = "Noise Texture.010"
    noise_texture_010.noise_dimensions = "4D"
    noise_texture_010.noise_type = "HETERO_TERRAIN"
    noise_texture_010.normalize = True
    # Vector
    noise_texture_010.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Detail
    noise_texture_010.inputs[3].default_value = 15.0
    # Distortion
    noise_texture_010.inputs[8].default_value = 0.0

    # node Group.017
    group_017 = martianterrain.nodes.new("GeometryNodeGroup")
    group_017.name = "Group.017"
    group_017.node_tree = random__uniform_
    # Socket_1
    group_017.inputs[0].default_value = -100000000.0
    # Socket_2
    group_017.inputs[1].default_value = 1000000000.0
    # Socket_4
    group_017.inputs[3].default_value = 7859

    # node Reroute.010
    reroute_010_1 = martianterrain.nodes.new("NodeReroute")
    reroute_010_1.name = "Reroute.010"
    # node Group.018
    group_018 = martianterrain.nodes.new("GeometryNodeGroup")
    group_018.name = "Group.018"
    group_018.node_tree = random__normal_
    # Socket_1
    group_018.inputs[0].default_value = True
    # Socket_2
    group_018.inputs[1].default_value = 1.5
    # Socket_3
    group_018.inputs[2].default_value = 0.25
    # Socket_5
    group_018.inputs[4].default_value = 543

    # node Group.020
    group_020 = martianterrain.nodes.new("GeometryNodeGroup")
    group_020.name = "Group.020"
    group_020.node_tree = random__normal_
    # Socket_1
    group_020.inputs[0].default_value = True
    # Socket_2
    group_020.inputs[1].default_value = 0.22499999403953552
    # Socket_3
    group_020.inputs[2].default_value = 0.02500000037252903
    # Socket_5
    group_020.inputs[4].default_value = 10032

    # node Group.021
    group_021 = martianterrain.nodes.new("GeometryNodeGroup")
    group_021.name = "Group.021"
    group_021.node_tree = random__normal_
    # Socket_1
    group_021.inputs[0].default_value = True
    # Socket_2
    group_021.inputs[1].default_value = 3.0
    # Socket_3
    group_021.inputs[2].default_value = 0.5
    # Socket_5
    group_021.inputs[4].default_value = 6515

    # node Frame.005
    frame_005_1 = martianterrain.nodes.new("NodeFrame")
    frame_005_1.name = "Frame.005"
    frame_005_1.label_size = 20
    frame_005_1.shrink = True

    # node Noise Texture.011
    noise_texture_011_1 = martianterrain.nodes.new("ShaderNodeTexNoise")
    noise_texture_011_1.name = "Noise Texture.011"
    noise_texture_011_1.noise_dimensions = "4D"
    noise_texture_011_1.noise_type = "FBM"
    noise_texture_011_1.normalize = True
    # Vector
    noise_texture_011_1.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Detail
    noise_texture_011_1.inputs[3].default_value = 15.0
    # Distortion
    noise_texture_011_1.inputs[8].default_value = 0.0

    # node Group.019
    group_019_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_019_1.name = "Group.019"
    group_019_1.node_tree = random__uniform_
    # Socket_1
    group_019_1.inputs[0].default_value = -100000000.0
    # Socket_2
    group_019_1.inputs[1].default_value = 1000000000.0
    # Socket_4
    group_019_1.inputs[3].default_value = 76322

    # node Reroute.011
    reroute_011 = martianterrain.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    # node Group.022
    group_022_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_022_1.name = "Group.022"
    group_022_1.node_tree = random__normal_
    # Socket_1
    group_022_1.inputs[0].default_value = True
    # Socket_2
    group_022_1.inputs[1].default_value = 2.0
    # Socket_3
    group_022_1.inputs[2].default_value = 0.10000000149011612
    # Socket_5
    group_022_1.inputs[4].default_value = 23556

    # node Group.023
    group_023_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_023_1.name = "Group.023"
    group_023_1.node_tree = random__normal_
    # Socket_1
    group_023_1.inputs[0].default_value = True
    # Socket_2
    group_023_1.inputs[1].default_value = 0.18000000715255737
    # Socket_3
    group_023_1.inputs[2].default_value = 0.03999999910593033
    # Socket_5
    group_023_1.inputs[4].default_value = 8479

    # node Group.024
    group_024_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_024_1.name = "Group.024"
    group_024_1.node_tree = random__normal_
    # Socket_1
    group_024_1.inputs[0].default_value = True
    # Socket_2
    group_024_1.inputs[1].default_value = 3.25
    # Socket_3
    group_024_1.inputs[2].default_value = 0.25
    # Socket_5
    group_024_1.inputs[4].default_value = 12594

    # node Frame.006
    frame_006 = martianterrain.nodes.new("NodeFrame")
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    # node Group.026
    group_026 = martianterrain.nodes.new("GeometryNodeGroup")
    group_026.name = "Group.026"
    group_026.node_tree = random__normal_
    # Socket_1
    group_026.inputs[0].default_value = True
    # Socket_2
    group_026.inputs[1].default_value = 0.5
    # Socket_3
    group_026.inputs[2].default_value = 0.20000000298023224
    # Socket_5
    group_026.inputs[4].default_value = 521

    # node Set Position.005
    set_position_005 = martianterrain.nodes.new("GeometryNodeSetPosition")
    set_position_005.name = "Set Position.005"
    set_position_005.inputs[1].hide = True
    set_position_005.inputs[2].hide = True
    # Selection
    set_position_005.inputs[1].default_value = True
    # Position
    set_position_005.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Math.002
    math_002_2 = martianterrain.nodes.new("ShaderNodeMath")
    math_002_2.name = "Math.002"
    math_002_2.operation = "ADD"
    math_002_2.use_clamp = False

    # node Math.003
    math_003_2 = martianterrain.nodes.new("ShaderNodeMath")
    math_003_2.name = "Math.003"
    math_003_2.operation = "ADD"
    math_003_2.use_clamp = False

    # node Combine XYZ.002
    combine_xyz_002 = martianterrain.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    # X
    combine_xyz_002.inputs[0].default_value = 0.0
    # Y
    combine_xyz_002.inputs[1].default_value = 0.0

    # node Vector
    vector = martianterrain.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (0.0, 0.0, 5.0)

    # node Transform Geometry
    transform_geometry_1 = martianterrain.nodes.new("GeometryNodeTransform")
    transform_geometry_1.name = "Transform Geometry"
    transform_geometry_1.mode = "COMPONENTS"
    transform_geometry_1.inputs[2].hide = True
    transform_geometry_1.inputs[3].hide = True
    transform_geometry_1.inputs[4].hide = True
    # Rotation
    transform_geometry_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_1.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Float Curve
    float_curve_1 = martianterrain.nodes.new("ShaderNodeFloatCurve")
    float_curve_1.name = "Float Curve"
    # mapping settings
    float_curve_1.mapping.extend = "EXTRAPOLATED"
    float_curve_1.mapping.tone = "STANDARD"
    float_curve_1.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_1.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_1.mapping.clip_min_x = 0.0
    float_curve_1.mapping.clip_min_y = 0.0
    float_curve_1.mapping.clip_max_x = 1.0
    float_curve_1.mapping.clip_max_y = 1.0
    float_curve_1.mapping.use_clip = True
    # curve 0
    float_curve_1_curve_0 = float_curve_1.mapping.curves[0]
    float_curve_1_curve_0_point_0 = float_curve_1_curve_0.points[0]
    float_curve_1_curve_0_point_0.location = (0.0, 1.0)
    float_curve_1_curve_0_point_0.handle_type = "AUTO"
    float_curve_1_curve_0_point_1 = float_curve_1_curve_0.points[1]
    float_curve_1_curve_0_point_1.location = (0.02500000037252903, 0.9750000238418579)
    float_curve_1_curve_0_point_1.handle_type = "AUTO"
    float_curve_1_curve_0_point_2 = float_curve_1_curve_0.points.new(
        0.5, 0.10000000149011612
    )
    float_curve_1_curve_0_point_2.handle_type = "AUTO_CLAMPED"
    float_curve_1_curve_0_point_3 = float_curve_1_curve_0.points.new(1.0, 0.0)
    float_curve_1_curve_0_point_3.handle_type = "AUTO"
    # update curve after changes
    float_curve_1.mapping.update()
    # Factor
    float_curve_1.inputs[0].default_value = 1.0

    # node Reroute
    reroute_1 = martianterrain.nodes.new("NodeReroute")
    reroute_1.name = "Reroute"
    # node Frame.007
    frame_007 = martianterrain.nodes.new("NodeFrame")
    frame_007.label = "Surface displacement"
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    # node Reroute.012
    reroute_012_1 = martianterrain.nodes.new("NodeReroute")
    reroute_012_1.name = "Reroute.012"
    # node Transform Geometry.002
    transform_geometry_002_1 = martianterrain.nodes.new("GeometryNodeTransform")
    transform_geometry_002_1.name = "Transform Geometry.002"
    transform_geometry_002_1.mode = "COMPONENTS"
    transform_geometry_002_1.inputs[1].hide = True
    transform_geometry_002_1.inputs[2].hide = True
    transform_geometry_002_1.inputs[4].hide = True
    # Translation
    transform_geometry_002_1.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_002_1.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Attribute Statistic.002
    attribute_statistic_002 = martianterrain.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_002.name = "Attribute Statistic.002"
    attribute_statistic_002.data_type = "FLOAT_VECTOR"
    attribute_statistic_002.domain = "POINT"
    attribute_statistic_002.inputs[1].hide = True
    attribute_statistic_002.outputs[0].hide = True
    attribute_statistic_002.outputs[1].hide = True
    attribute_statistic_002.outputs[2].hide = True
    attribute_statistic_002.outputs[3].hide = True
    attribute_statistic_002.outputs[4].hide = True
    attribute_statistic_002.outputs[6].hide = True
    attribute_statistic_002.outputs[7].hide = True
    # Selection
    attribute_statistic_002.inputs[1].default_value = True

    # node Position.005
    position_005 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_005.name = "Position.005"

    # node Reroute.013
    reroute_013_1 = martianterrain.nodes.new("NodeReroute")
    reroute_013_1.name = "Reroute.013"
    # node Vector Math.030
    vector_math_030 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_030.name = "Vector Math.030"
    vector_math_030.operation = "DIVIDE"
    # Vector
    vector_math_030.inputs[0].default_value = (1.0, 1.0, 1.0)

    # node Frame.008
    frame_008 = martianterrain.nodes.new("NodeFrame")
    frame_008.label = "Normalize height"
    frame_008.name = "Frame.008"
    frame_008.label_size = 20
    frame_008.shrink = True

    # node Separate XYZ.001
    separate_xyz_001_1 = martianterrain.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001_1.name = "Separate XYZ.001"
    separate_xyz_001_1.mute = True
    separate_xyz_001_1.outputs[2].hide = True

    # node Math.006
    math_006_1 = martianterrain.nodes.new("ShaderNodeMath")
    math_006_1.name = "Math.006"
    math_006_1.mute = True
    math_006_1.operation = "MULTIPLY"
    math_006_1.use_clamp = False

    # node Math.009
    math_009 = martianterrain.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = "MAXIMUM"
    math_009.use_clamp = False

    # node Math.010
    math_010_1 = martianterrain.nodes.new("ShaderNodeMath")
    math_010_1.name = "Math.010"
    math_010_1.operation = "DIVIDE"
    math_010_1.use_clamp = False

    # node Math.011
    math_011 = martianterrain.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = "DIVIDE"
    math_011.use_clamp = False

    # node Mix
    mix = martianterrain.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.mute = True
    mix.blend_type = "MIX"
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = "FLOAT"
    mix.factor_mode = "UNIFORM"
    mix.inputs[0].hide = True
    mix.inputs[1].hide = True
    mix.inputs[4].hide = True
    mix.inputs[5].hide = True
    mix.inputs[6].hide = True
    mix.inputs[7].hide = True
    mix.inputs[8].hide = True
    mix.inputs[9].hide = True
    mix.outputs[1].hide = True
    mix.outputs[2].hide = True
    mix.outputs[3].hide = True
    # Factor_Float
    mix.inputs[0].default_value = 0.5

    # node Math.007
    math_007_1 = martianterrain.nodes.new("ShaderNodeMath")
    math_007_1.name = "Math.007"
    math_007_1.mute = True
    math_007_1.operation = "MULTIPLY"
    math_007_1.use_clamp = False

    # node Reroute.002
    reroute_002_2 = martianterrain.nodes.new("NodeReroute")
    reroute_002_2.name = "Reroute.002"
    reroute_002_2.mute = True
    # node Reroute.014
    reroute_014 = martianterrain.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    # node Reroute.015
    reroute_015_1 = martianterrain.nodes.new("NodeReroute")
    reroute_015_1.name = "Reroute.015"
    # node Group.002
    group_002_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_002_1.name = "Group.002"
    group_002_1.mute = True
    group_002_1.node_tree = random__normal_
    # Socket_1
    group_002_1.inputs[0].default_value = True
    # Socket_2
    group_002_1.inputs[1].default_value = 0.6000000238418579
    # Socket_3
    group_002_1.inputs[2].default_value = 0.20000000298023224
    # Socket_5
    group_002_1.inputs[4].default_value = 65241

    # node Group.003
    group_003_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_003_1.name = "Group.003"
    group_003_1.mute = True
    group_003_1.node_tree = random__normal_
    # Socket_1
    group_003_1.inputs[0].default_value = True
    # Socket_2
    group_003_1.inputs[1].default_value = 0.3333333432674408
    # Socket_3
    group_003_1.inputs[2].default_value = 0.0833333358168602
    # Socket_5
    group_003_1.inputs[4].default_value = 87654

    # node Group.004
    group_004_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_004_1.name = "Group.004"
    group_004_1.mute = True
    group_004_1.node_tree = random__normal_
    # Socket_1
    group_004_1.inputs[0].default_value = True
    # Socket_2
    group_004_1.inputs[1].default_value = 0.8999999761581421
    # Socket_3
    group_004_1.inputs[2].default_value = 0.20000000298023224
    # Socket_5
    group_004_1.inputs[4].default_value = 521

    # node Group.005
    group_005_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_005_1.name = "Group.005"
    group_005_1.mute = True
    group_005_1.node_tree = random__normal_
    # Socket_1
    group_005_1.inputs[0].default_value = True
    # Socket_2
    group_005_1.inputs[1].default_value = 0.75
    # Socket_3
    group_005_1.inputs[2].default_value = 0.25
    # Socket_5
    group_005_1.inputs[4].default_value = 215

    # node Reroute.016
    reroute_016 = martianterrain.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.mute = True
    # node Group.001
    group_001_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_001_1.name = "Group.001"
    group_001_1.node_tree = martianrock
    # Socket_3
    group_001_1.inputs[2].default_value = (1.0, 1.0, 1.0)
    # Socket_4
    group_001_1.inputs[3].default_value = (0.25, 0.25, 0.10000000149011612)
    # Socket_5
    group_001_1.inputs[4].default_value = False
    # Socket_6
    group_001_1.inputs[5].default_value = 0.0

    # node Distribute Points on Faces
    distribute_points_on_faces = martianterrain.nodes.new(
        "GeometryNodeDistributePointsOnFaces"
    )
    distribute_points_on_faces.name = "Distribute Points on Faces"
    distribute_points_on_faces.distribute_method = "POISSON"
    distribute_points_on_faces.use_legacy_normal = False
    # Selection
    distribute_points_on_faces.inputs[1].default_value = True
    # Density Max
    distribute_points_on_faces.inputs[3].default_value = 2.0

    # node Repeat Input
    repeat_input = martianterrain.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    # node Repeat Output
    repeat_output = martianterrain.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.active_index = 1
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new("GEOMETRY", "Geometry")
    # Create item "Point Index"
    repeat_output.repeat_items.new("INT", "Point Index")

    # node Math.004
    math_004_2 = martianterrain.nodes.new("ShaderNodeMath")
    math_004_2.name = "Math.004"
    math_004_2.operation = "ADD"
    math_004_2.use_clamp = False
    # Value_001
    math_004_2.inputs[1].default_value = 1.0

    # node Domain Size
    domain_size = martianterrain.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.component = "POINTCLOUD"

    # node Join Geometry.001
    join_geometry_001 = martianterrain.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    # node Join Geometry
    join_geometry = martianterrain.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # node Sample Index
    sample_index = martianterrain.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.clamp = False
    sample_index.data_type = "FLOAT_VECTOR"
    sample_index.domain = "POINT"

    # node Position
    position_1 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_1.name = "Position"

    # node Transform Geometry.003
    transform_geometry_003_1 = martianterrain.nodes.new("GeometryNodeTransform")
    transform_geometry_003_1.name = "Transform Geometry.003"
    transform_geometry_003_1.mode = "COMPONENTS"
    transform_geometry_003_1.inputs[2].hide = True
    transform_geometry_003_1.inputs[4].hide = True
    # Rotation
    transform_geometry_003_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_003_1.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Group.006
    group_006_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_006_1.name = "Group.006"
    group_006_1.node_tree = random__uniform_
    # Socket_1
    group_006_1.inputs[0].default_value = 0.0
    # Socket_2
    group_006_1.inputs[1].default_value = 100000.0
    # Socket_4
    group_006_1.inputs[3].default_value = 434

    # node Float to Integer.002
    float_to_integer_002 = martianterrain.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_002.name = "Float to Integer.002"
    float_to_integer_002.rounding_mode = "ROUND"

    # node Math.005
    math_005_2 = martianterrain.nodes.new("ShaderNodeMath")
    math_005_2.name = "Math.005"
    math_005_2.operation = "ADD"
    math_005_2.use_clamp = False

    # node Reroute.018
    reroute_018_1 = martianterrain.nodes.new("NodeReroute")
    reroute_018_1.label = "Index"
    reroute_018_1.name = "Reroute.018"
    # node Reroute.019
    reroute_019_1 = martianterrain.nodes.new("NodeReroute")
    reroute_019_1.label = "Seed"
    reroute_019_1.name = "Reroute.019"
    # node Group.007
    group_007_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_007_1.name = "Group.007"
    group_007_1.node_tree = random__uniform_
    # Socket_1
    group_007_1.inputs[0].default_value = 0.0
    # Socket_2
    group_007_1.inputs[1].default_value = 1.0
    # Socket_4
    group_007_1.inputs[3].default_value = 76543

    # node Float Curve.001
    float_curve_001 = martianterrain.nodes.new("ShaderNodeFloatCurve")
    float_curve_001.name = "Float Curve.001"
    # mapping settings
    float_curve_001.mapping.extend = "EXTRAPOLATED"
    float_curve_001.mapping.tone = "STANDARD"
    float_curve_001.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_001.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_001.mapping.clip_min_x = 0.0
    float_curve_001.mapping.clip_min_y = 0.0
    float_curve_001.mapping.clip_max_x = 1.0
    float_curve_001.mapping.clip_max_y = 1.0
    float_curve_001.mapping.use_clip = True
    # curve 0
    float_curve_001_curve_0 = float_curve_001.mapping.curves[0]
    float_curve_001_curve_0_point_0 = float_curve_001_curve_0.points[0]
    float_curve_001_curve_0_point_0.location = (0.0, 0.019999999552965164)
    float_curve_001_curve_0_point_0.handle_type = "AUTO_CLAMPED"
    float_curve_001_curve_0_point_1 = float_curve_001_curve_0.points[1]
    float_curve_001_curve_0_point_1.location = (0.25, 0.019999999552965164)
    float_curve_001_curve_0_point_1.handle_type = "AUTO_CLAMPED"
    float_curve_001_curve_0_point_2 = float_curve_001_curve_0.points.new(
        0.949999988079071, 0.20000000298023224
    )
    float_curve_001_curve_0_point_2.handle_type = "AUTO_CLAMPED"
    float_curve_001_curve_0_point_3 = float_curve_001_curve_0.points.new(1.0, 1.0)
    float_curve_001_curve_0_point_3.handle_type = "AUTO_CLAMPED"
    # update curve after changes
    float_curve_001.mapping.update()
    # Factor
    float_curve_001.inputs[0].default_value = 1.0

    # node Delete Geometry
    delete_geometry_1 = martianterrain.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_1.name = "Delete Geometry"
    delete_geometry_1.domain = "POINT"
    delete_geometry_1.mode = "ALL"

    # node Position.001
    position_001_1 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_001_1.name = "Position.001"

    # node Compare.001
    compare_001_1 = martianterrain.nodes.new("FunctionNodeCompare")
    compare_001_1.name = "Compare.001"
    compare_001_1.data_type = "FLOAT"
    compare_001_1.mode = "ELEMENT"
    compare_001_1.operation = "GREATER_THAN"

    # node Separate XYZ.002
    separate_xyz_002_1 = martianterrain.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002_1.name = "Separate XYZ.002"
    separate_xyz_002_1.outputs[2].hide = True

    # node Compare.002
    compare_002 = martianterrain.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = "FLOAT"
    compare_002.mode = "ELEMENT"
    compare_002.operation = "GREATER_THAN"

    # node Math.008
    math_008_1 = martianterrain.nodes.new("ShaderNodeMath")
    math_008_1.name = "Math.008"
    math_008_1.operation = "ABSOLUTE"
    math_008_1.use_clamp = False

    # node Math.012
    math_012 = martianterrain.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = "ABSOLUTE"
    math_012.use_clamp = False

    # node Boolean Math
    boolean_math_1 = martianterrain.nodes.new("FunctionNodeBooleanMath")
    boolean_math_1.name = "Boolean Math"
    boolean_math_1.operation = "OR"

    # node Separate XYZ.003
    separate_xyz_003_1 = martianterrain.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003_1.name = "Separate XYZ.003"
    separate_xyz_003_1.outputs[2].hide = True

    # node Math.013
    math_013 = martianterrain.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = "MULTIPLY"
    math_013.use_clamp = False
    # Value_001
    math_013.inputs[1].default_value = 0.44999998807907104

    # node Math.014
    math_014 = martianterrain.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = "MULTIPLY"
    math_014.use_clamp = False
    # Value_001
    math_014.inputs[1].default_value = 0.44999998807907104

    # node Vector Math
    vector_math_1 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_1.name = "Vector Math"
    vector_math_1.operation = "ADD"

    # node Frame.010
    frame_010 = martianterrain.nodes.new("NodeFrame")
    frame_010.label = "sample points (not in flat centre or boundaries)"
    frame_010.name = "Frame.010"
    frame_010.label_size = 20
    frame_010.shrink = True

    # node Frame.011
    frame_011 = martianterrain.nodes.new("NodeFrame")
    frame_011.label = "rocks"
    frame_011.name = "Frame.011"
    frame_011.mute = True
    frame_011.label_size = 20
    frame_011.shrink = True

    # node Frame.012
    frame_012 = martianterrain.nodes.new("NodeFrame")
    frame_012.label = "Displace current position based on distance to crater center"
    frame_012.name = "Frame.012"
    frame_012.mute = True
    frame_012.label_size = 20
    frame_012.shrink = True

    # node Frame.013
    frame_013 = martianterrain.nodes.new("NodeFrame")
    frame_013.label = "Subtract zero point of curve to avoid offsetting crater edge"
    frame_013.name = "Frame.013"
    frame_013.mute = True
    frame_013.label_size = 20
    frame_013.shrink = True

    # node Frame.014
    frame_014 = martianterrain.nodes.new("NodeFrame")
    frame_014.label = "Only offset vertices within the radius of the nearest crater"
    frame_014.name = "Frame.014"
    frame_014.mute = True
    frame_014.label_size = 20
    frame_014.shrink = True

    # node Frame.015
    frame_015 = martianterrain.nodes.new("NodeFrame")
    frame_015.label = "Sample crater points"
    frame_015.name = "Frame.015"
    frame_015.mute = True
    frame_015.label_size = 20
    frame_015.shrink = True

    # node Math.016
    math_016 = martianterrain.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.mute = True
    math_016.operation = "MULTIPLY"
    math_016.use_clamp = False
    # Value_001
    math_016.inputs[1].default_value = 1.7999999523162842

    # node Position.006
    position_006 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_006.name = "Position.006"
    position_006.mute = True

    # node Math.017
    math_017 = martianterrain.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.mute = True
    math_017.operation = "MULTIPLY"
    math_017.use_clamp = False

    # node Vector Math.001
    vector_math_001_1 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_001_1.name = "Vector Math.001"
    vector_math_001_1.mute = True
    vector_math_001_1.operation = "DISTANCE"

    # node Math.018
    math_018 = martianterrain.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.mute = True
    math_018.operation = "DIVIDE"
    math_018.use_clamp = False

    # node Math.019
    math_019 = martianterrain.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.mute = True
    math_019.operation = "SUBTRACT"
    math_019.use_clamp = False
    # Value
    math_019.inputs[0].default_value = 1.0

    # node Set Position
    set_position_1 = martianterrain.nodes.new("GeometryNodeSetPosition")
    set_position_1.name = "Set Position"
    set_position_1.mute = True
    set_position_1.inputs[3].hide = True
    # Offset
    set_position_1.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Math.020
    math_020 = martianterrain.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.mute = True
    math_020.operation = "MULTIPLY"
    math_020.use_clamp = False

    # node Math.021
    math_021 = martianterrain.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.mute = True
    math_021.operation = "MULTIPLY"
    math_021.use_clamp = False

    # node Compare.003
    compare_003 = martianterrain.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.mute = True
    compare_003.data_type = "FLOAT"
    compare_003.mode = "ELEMENT"
    compare_003.operation = "LESS_THAN"
    # B
    compare_003.inputs[1].default_value = 1.0

    # node Group.008
    group_008_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_008_1.name = "Group.008"
    group_008_1.mute = True
    group_008_1.node_tree = crater_profile

    # node Math.022
    math_022 = martianterrain.nodes.new("ShaderNodeMath")
    math_022.name = "Math.022"
    math_022.mute = True
    math_022.operation = "SUBTRACT"
    math_022.use_clamp = False

    # node Group.009
    group_009_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_009_1.name = "Group.009"
    group_009_1.mute = True
    group_009_1.node_tree = crater_profile
    # Socket_1
    group_009_1.inputs[0].default_value = 0.0

    # node Distribute Points on Faces.001
    distribute_points_on_faces_001 = martianterrain.nodes.new(
        "GeometryNodeDistributePointsOnFaces"
    )
    distribute_points_on_faces_001.name = "Distribute Points on Faces.001"
    distribute_points_on_faces_001.mute = True
    distribute_points_on_faces_001.distribute_method = "POISSON"
    distribute_points_on_faces_001.use_legacy_normal = True
    # Selection
    distribute_points_on_faces_001.inputs[1].default_value = True
    # Density Max
    distribute_points_on_faces_001.inputs[3].default_value = 1.0

    # node Random Value
    random_value_1 = martianterrain.nodes.new("FunctionNodeRandomValue")
    random_value_1.name = "Random Value"
    random_value_1.mute = True
    random_value_1.data_type = "FLOAT"
    # Min_001
    random_value_1.inputs[2].default_value = 0.0
    # Max_001
    random_value_1.inputs[3].default_value = 1.0
    # ID
    random_value_1.inputs[7].default_value = 0

    # node Sample Index.001
    sample_index_001 = martianterrain.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.mute = True
    sample_index_001.clamp = False
    sample_index_001.data_type = "FLOAT_VECTOR"
    sample_index_001.domain = "POINT"

    # node Sample Nearest
    sample_nearest = martianterrain.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.mute = True
    sample_nearest.domain = "POINT"
    # Sample Position
    sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)

    # node Sample Index.002
    sample_index_002 = martianterrain.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.mute = True
    sample_index_002.clamp = False
    sample_index_002.data_type = "FLOAT"
    sample_index_002.domain = "POINT"

    # node Sample Nearest.001
    sample_nearest_001 = martianterrain.nodes.new("GeometryNodeSampleNearest")
    sample_nearest_001.name = "Sample Nearest.001"
    sample_nearest_001.mute = True
    sample_nearest_001.domain = "POINT"
    # Sample Position
    sample_nearest_001.inputs[1].default_value = (0.0, 0.0, 0.0)

    # node Mix.001
    mix_001 = martianterrain.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.mute = True
    mix_001.blend_type = "MIX"
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = "VECTOR"
    mix_001.factor_mode = "UNIFORM"
    # A_Vector
    mix_001.inputs[4].default_value = (0.0, 0.0, 1.0)

    # node Combine XYZ.003
    combine_xyz_003 = martianterrain.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.mute = True
    combine_xyz_003.inputs[2].hide = True
    # Z
    combine_xyz_003.inputs[2].default_value = 0.0

    # node Separate XYZ.004
    separate_xyz_004 = martianterrain.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_004.name = "Separate XYZ.004"
    separate_xyz_004.mute = True
    separate_xyz_004.outputs[2].hide = True

    # node Combine XYZ.004
    combine_xyz_004 = martianterrain.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.mute = True
    combine_xyz_004.inputs[2].hide = True
    # Z
    combine_xyz_004.inputs[2].default_value = 0.0

    # node Separate XYZ.005
    separate_xyz_005 = martianterrain.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_005.name = "Separate XYZ.005"
    separate_xyz_005.mute = True
    separate_xyz_005.outputs[2].hide = True

    # node Math.023
    math_023 = martianterrain.nodes.new("ShaderNodeMath")
    math_023.name = "Math.023"
    math_023.mute = True
    math_023.operation = "ADD"
    math_023.use_clamp = False
    # Value_001
    math_023.inputs[1].default_value = 1.0

    # node Vector Math.003
    vector_math_003_1 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_003_1.name = "Vector Math.003"
    vector_math_003_1.mute = True
    vector_math_003_1.operation = "MULTIPLY"

    # node Sample Index.003
    sample_index_003 = martianterrain.nodes.new("GeometryNodeSampleIndex")
    sample_index_003.name = "Sample Index.003"
    sample_index_003.mute = True
    sample_index_003.clamp = False
    sample_index_003.data_type = "FLOAT_VECTOR"
    sample_index_003.domain = "POINT"

    # node String
    string = martianterrain.nodes.new("FunctionNodeInputString")
    string.name = "String"
    string.mute = True
    string.string = "crater_normal"

    # node Reroute.017
    reroute_017_1 = martianterrain.nodes.new("NodeReroute")
    reroute_017_1.name = "Reroute.017"
    reroute_017_1.mute = True
    # node Reroute.020
    reroute_020_1 = martianterrain.nodes.new("NodeReroute")
    reroute_020_1.name = "Reroute.020"
    reroute_020_1.mute = True
    # node Reroute.021
    reroute_021_1 = martianterrain.nodes.new("NodeReroute")
    reroute_021_1.name = "Reroute.021"
    reroute_021_1.mute = True
    # node Reroute.022
    reroute_022_1 = martianterrain.nodes.new("NodeReroute")
    reroute_022_1.name = "Reroute.022"
    reroute_022_1.mute = True
    # node Reroute.023
    reroute_023 = martianterrain.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    reroute_023.mute = True
    # node Store Named Attribute
    store_named_attribute = martianterrain.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.mute = True
    store_named_attribute.data_type = "FLOAT_VECTOR"
    store_named_attribute.domain = "POINT"
    # Selection
    store_named_attribute.inputs[1].default_value = True

    # node Store Named Attribute.001
    store_named_attribute_001 = martianterrain.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.mute = True
    store_named_attribute_001.data_type = "FLOAT"
    store_named_attribute_001.domain = "POINT"
    # Selection
    store_named_attribute_001.inputs[1].default_value = True

    # node Named Attribute
    named_attribute = martianterrain.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.mute = True
    named_attribute.data_type = "FLOAT"

    # node Named Attribute.001
    named_attribute_001 = martianterrain.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.mute = True
    named_attribute_001.data_type = "FLOAT_VECTOR"

    # node String.001
    string_001 = martianterrain.nodes.new("FunctionNodeInputString")
    string_001.name = "String.001"
    string_001.mute = True
    string_001.string = "crater_radius"

    # node Float Curve.002
    float_curve_002 = martianterrain.nodes.new("ShaderNodeFloatCurve")
    float_curve_002.label = "Crater size distribution"
    float_curve_002.name = "Float Curve.002"
    float_curve_002.mute = True
    # mapping settings
    float_curve_002.mapping.extend = "EXTRAPOLATED"
    float_curve_002.mapping.tone = "STANDARD"
    float_curve_002.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_002.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_002.mapping.clip_min_x = 0.0
    float_curve_002.mapping.clip_min_y = 0.0
    float_curve_002.mapping.clip_max_x = 1.0
    float_curve_002.mapping.clip_max_y = 1.0
    float_curve_002.mapping.use_clip = True
    # curve 0
    float_curve_002_curve_0 = float_curve_002.mapping.curves[0]
    float_curve_002_curve_0_point_0 = float_curve_002_curve_0.points[0]
    float_curve_002_curve_0_point_0.location = (0.0, 0.02500000037252903)
    float_curve_002_curve_0_point_0.handle_type = "AUTO"
    float_curve_002_curve_0_point_1 = float_curve_002_curve_0.points[1]
    float_curve_002_curve_0_point_1.location = (0.8136363625526428, 0.08124995976686478)
    float_curve_002_curve_0_point_1.handle_type = "AUTO"
    float_curve_002_curve_0_point_2 = float_curve_002_curve_0.points.new(
        0.9318180680274963, 0.10000011324882507
    )
    float_curve_002_curve_0_point_2.handle_type = "AUTO"
    float_curve_002_curve_0_point_3 = float_curve_002_curve_0.points.new(1.0, 1.0)
    float_curve_002_curve_0_point_3.handle_type = "AUTO"
    # update curve after changes
    float_curve_002.mapping.update()
    # Factor
    float_curve_002.inputs[0].default_value = 1.0

    # node Reroute.025
    reroute_025 = martianterrain.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.mute = True
    # node Reroute.026
    reroute_026 = martianterrain.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    reroute_026.mute = True
    # node Position.007
    position_007 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_007.name = "Position.007"
    position_007.mute = True

    # node Vector Math.004
    vector_math_004_1 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_004_1.name = "Vector Math.004"
    vector_math_004_1.mute = True
    vector_math_004_1.operation = "ADD"

    # node Reroute.027
    reroute_027 = martianterrain.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    reroute_027.mute = True
    # node Math.024
    math_024 = martianterrain.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.mute = True
    math_024.operation = "MULTIPLY"
    math_024.use_clamp = False

    # node Math.025
    math_025 = martianterrain.nodes.new("ShaderNodeMath")
    math_025.name = "Math.025"
    math_025.mute = True
    math_025.operation = "SUBTRACT"
    math_025.use_clamp = False
    # Value
    math_025.inputs[0].default_value = 1.0

    # node Frame.016
    frame_016 = martianterrain.nodes.new("NodeFrame")
    frame_016.label = "Craters"
    frame_016.name = "Frame.016"
    frame_016.mute = True
    frame_016.label_size = 20
    frame_016.shrink = True

    # node Frame.017
    frame_017 = martianterrain.nodes.new("NodeFrame")
    frame_017.label = "terrain"
    frame_017.name = "Frame.017"
    frame_017.label_size = 20
    frame_017.shrink = True

    # node Reroute.028
    reroute_028 = martianterrain.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    reroute_028.mute = True
    # node Reroute.031
    reroute_031 = martianterrain.nodes.new("NodeReroute")
    reroute_031.name = "Reroute.031"
    # node Reroute.033
    reroute_033 = martianterrain.nodes.new("NodeReroute")
    reroute_033.name = "Reroute.033"
    # node Reroute.032
    reroute_032 = martianterrain.nodes.new("NodeReroute")
    reroute_032.name = "Reroute.032"
    # node Reroute.029
    reroute_029 = martianterrain.nodes.new("NodeReroute")
    reroute_029.name = "Reroute.029"
    reroute_029.mute = True
    # node Reroute.030
    reroute_030 = martianterrain.nodes.new("NodeReroute")
    reroute_030.name = "Reroute.030"
    reroute_030.mute = True
    # node Frame.009
    frame_009 = martianterrain.nodes.new("NodeFrame")
    frame_009.name = "Frame.009"
    frame_009.use_custom_color = True
    frame_009.color = (0.6079999804496765, 0.0, 0.014633849263191223)
    frame_009.mute = True
    frame_009.label_size = 20
    frame_009.shrink = True

    # node Frame.018
    frame_018 = martianterrain.nodes.new("NodeFrame")
    frame_018.name = "Frame.018"
    frame_018.use_custom_color = True
    frame_018.color = (0.6079999804496765, 0.0, 0.043328672647476196)
    frame_018.label_size = 20
    frame_018.shrink = True

    # node Reroute.024
    reroute_024 = martianterrain.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.mute = True
    # node Frame.019
    frame_019 = martianterrain.nodes.new("NodeFrame")
    frame_019.label = "Max crater size"
    frame_019.name = "Frame.019"
    frame_019.mute = True
    frame_019.label_size = 20
    frame_019.shrink = True

    # node Reroute.035
    reroute_035 = martianterrain.nodes.new("NodeReroute")
    reroute_035.name = "Reroute.035"
    reroute_035.mute = True
    # node Boolean Math.001
    boolean_math_001 = martianterrain.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = "OR"

    # node Combine XYZ.005
    combine_xyz_005 = martianterrain.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.inputs[2].hide = True
    # Z
    combine_xyz_005.inputs[2].default_value = 0.0

    # node Vector Math.005
    vector_math_005 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.operation = "LENGTH"

    # node Compare.004
    compare_004 = martianterrain.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = "FLOAT"
    compare_004.mode = "ELEMENT"
    compare_004.operation = "LESS_THAN"

    # node Reroute.034
    reroute_034 = martianterrain.nodes.new("NodeReroute")
    reroute_034.name = "Reroute.034"
    # node Mix.002
    mix_002 = martianterrain.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = "MIX"
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = "FLOAT"
    mix_002.factor_mode = "UNIFORM"
    # Factor_Float
    mix_002.inputs[0].default_value = 0.5

    # node Math.026
    math_026 = martianterrain.nodes.new("ShaderNodeMath")
    math_026.name = "Math.026"
    math_026.operation = "MULTIPLY"
    math_026.use_clamp = False

    # node Group.010
    group_010_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_010_1.name = "Group.010"
    group_010_1.node_tree = random__normal_
    # Socket_1
    group_010_1.inputs[0].default_value = True
    # Socket_2
    group_010_1.inputs[1].default_value = 0.10000000149011612
    # Socket_3
    group_010_1.inputs[2].default_value = 0.02500000037252903
    # Socket_4
    group_010_1.inputs[3].default_value = 0
    # Socket_5
    group_010_1.inputs[4].default_value = 87702

    # node Math.027
    math_027 = martianterrain.nodes.new("ShaderNodeMath")
    math_027.label = "Minimum"
    math_027.name = "Math.027"
    math_027.operation = "MINIMUM"
    math_027.use_clamp = False

    # node Frame.020
    frame_020 = martianterrain.nodes.new("NodeFrame")
    frame_020.label = "rock size"
    frame_020.name = "Frame.020"
    frame_020.label_size = 20
    frame_020.shrink = True

    # node Math.028
    math_028 = martianterrain.nodes.new("ShaderNodeMath")
    math_028.name = "Math.028"
    math_028.operation = "MULTIPLY"
    math_028.use_clamp = False
    # Value_001
    math_028.inputs[1].default_value = 0.125

    # node Group.011
    group_011_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_011_1.name = "Group.011"
    group_011_1.node_tree = random__normal_
    # Socket_1
    group_011_1.inputs[0].default_value = True
    # Socket_2
    group_011_1.inputs[1].default_value = 0.75
    # Socket_3
    group_011_1.inputs[2].default_value = 0.125
    # Socket_5
    group_011_1.inputs[4].default_value = 6543

    # node Reroute.036
    reroute_036 = martianterrain.nodes.new("NodeReroute")
    reroute_036.name = "Reroute.036"
    # node Math.029
    math_029 = martianterrain.nodes.new("ShaderNodeMath")
    math_029.name = "Math.029"
    math_029.operation = "MULTIPLY"
    math_029.use_clamp = False

    # node Attribute Statistic
    attribute_statistic_1 = martianterrain.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_1.name = "Attribute Statistic"
    attribute_statistic_1.data_type = "FLOAT_VECTOR"
    attribute_statistic_1.domain = "POINT"
    attribute_statistic_1.inputs[1].hide = True
    attribute_statistic_1.outputs[0].hide = True
    attribute_statistic_1.outputs[1].hide = True
    attribute_statistic_1.outputs[2].hide = True
    attribute_statistic_1.outputs[3].hide = True
    attribute_statistic_1.outputs[4].hide = True
    attribute_statistic_1.outputs[6].hide = True
    attribute_statistic_1.outputs[7].hide = True
    # Selection
    attribute_statistic_1.inputs[1].default_value = True

    # node Position.008
    position_008 = martianterrain.nodes.new("GeometryNodeInputPosition")
    position_008.name = "Position.008"

    # node Separate XYZ.006
    separate_xyz_006 = martianterrain.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_006.name = "Separate XYZ.006"
    separate_xyz_006.outputs[0].hide = True
    separate_xyz_006.outputs[1].hide = True

    # node Combine XYZ.006
    combine_xyz_006 = martianterrain.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    combine_xyz_006.inputs[0].hide = True
    combine_xyz_006.inputs[1].hide = True
    # X
    combine_xyz_006.inputs[0].default_value = 0.0
    # Y
    combine_xyz_006.inputs[1].default_value = 0.0

    # node Transform Geometry.004
    transform_geometry_004 = martianterrain.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.mode = "COMPONENTS"
    transform_geometry_004.inputs[1].hide = True
    transform_geometry_004.inputs[2].hide = True
    transform_geometry_004.inputs[4].hide = True
    # Translation
    transform_geometry_004.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Vector Math.006
    vector_math_006 = martianterrain.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.operation = "SCALE"

    # node Group.012
    group_012_1 = martianterrain.nodes.new("GeometryNodeGroup")
    group_012_1.name = "Group.012"
    group_012_1.node_tree = random__uniform_
    # Socket_1
    group_012_1.inputs[0].default_value = 0.07500000298023224
    # Socket_2
    group_012_1.inputs[1].default_value = 0.25
    # Socket_4
    group_012_1.inputs[3].default_value = 214126

    # node Math.015
    math_015 = martianterrain.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = "DIVIDE"
    math_015.use_clamp = False

    # node Reroute.040
    reroute_040 = martianterrain.nodes.new("NodeReroute")
    reroute_040.name = "Reroute.040"
    # node Reroute.038
    reroute_038 = martianterrain.nodes.new("NodeReroute")
    reroute_038.name = "Reroute.038"
    # node Math.030
    math_030 = martianterrain.nodes.new("ShaderNodeMath")
    math_030.name = "Math.030"
    math_030.operation = "POWER"
    math_030.use_clamp = False
    # Value_001
    math_030.inputs[1].default_value = 0.5

    # node Float to Integer.001
    float_to_integer_001 = martianterrain.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_001.name = "Float to Integer.001"
    float_to_integer_001.rounding_mode = "FLOOR"

    # node Mesh Boolean
    mesh_boolean_1 = martianterrain.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_1.name = "Mesh Boolean"
    mesh_boolean_1.operation = "UNION"
    mesh_boolean_1.solver = "EXACT"
    # Self Intersection
    mesh_boolean_1.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_1.inputs[3].default_value = False

    # node Switch
    switch_2 = martianterrain.nodes.new("GeometryNodeSwitch")
    switch_2.name = "Switch"
    switch_2.input_type = "GEOMETRY"

    # node Reroute.037
    reroute_037 = martianterrain.nodes.new("NodeReroute")
    reroute_037.name = "Reroute.037"
    # node Reroute.039
    reroute_039 = martianterrain.nodes.new("NodeReroute")
    reroute_039.name = "Reroute.039"
    # node Reroute.041
    reroute_041 = martianterrain.nodes.new("NodeReroute")
    reroute_041.name = "Reroute.041"
    # node Value
    value = martianterrain.nodes.new("ShaderNodeValue")
    value.label = "Rock Size Limit"
    value.name = "Value"

    value.outputs[0].default_value = 2.0

    # Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)
    # Item_2
    repeat_input.inputs[2].default_value = 0

    # Set parents
    grid.parent = frame_001_2
    vector_math_012.parent = frame_002_1
    raycast.parent = frame_002_1
    frame_002_1.parent = frame_017
    vector_math_017.parent = frame_2
    gradient_texture_001.parent = frame_2
    position_002_1.parent = frame_2
    vector_math_019.parent = frame_2
    set_position_001_1.parent = frame_2
    position_003.parent = frame_2
    combine_xyz_1.parent = frame_2
    math_3.parent = frame_2
    reroute_001_1.parent = frame_002_1
    vector_math_002_1.parent = frame_001_2
    vector_math_021.parent = frame_001_2
    separate_xyz_1.parent = frame_001_2
    vector_math_023.parent = frame_001_2
    frame_001_2.parent = frame_017
    reroute_003_2.parent = frame_2
    compare_1.parent = frame_2
    transform_geometry_001_1.parent = frame_003_2
    attribute_statistic_001.parent = frame_003_2
    position_004_1.parent = frame_003_2
    reroute_007.parent = frame_003_2
    vector_math_028.parent = frame_003_2
    frame_003_2.parent = frame_017
    noise_texture_009.parent = frame_004_1
    group_013_1.parent = frame_004_1
    reroute_009.parent = frame_004_1
    group_2.parent = frame_004_1
    group_014_1.parent = frame_004_1
    group_015.parent = frame_004_1
    group_016.parent = frame_004_1
    frame_004_1.parent = frame_007
    noise_texture_010.parent = frame_005_1
    group_017.parent = frame_005_1
    reroute_010_1.parent = frame_005_1
    group_018.parent = frame_005_1
    group_020.parent = frame_005_1
    group_021.parent = frame_005_1
    frame_005_1.parent = frame_007
    noise_texture_011_1.parent = frame_006
    group_019_1.parent = frame_006
    reroute_011.parent = frame_006
    group_022_1.parent = frame_006
    group_023_1.parent = frame_006
    group_024_1.parent = frame_006
    frame_006.parent = frame_007
    group_026.parent = frame_005_1
    set_position_005.parent = frame_007
    math_002_2.parent = frame_004_1
    math_003_2.parent = frame_005_1
    combine_xyz_002.parent = frame_007
    vector.parent = frame_002_1
    transform_geometry_1.parent = frame_002_1
    float_curve_1.parent = frame_2
    reroute_1.parent = frame_003_2
    frame_007.parent = frame_017
    reroute_012_1.parent = frame_007
    transform_geometry_002_1.parent = frame_008
    attribute_statistic_002.parent = frame_008
    position_005.parent = frame_008
    reroute_013_1.parent = frame_008
    vector_math_030.parent = frame_008
    frame_008.parent = frame_017
    separate_xyz_001_1.parent = frame_019
    math_006_1.parent = frame_019
    math_009.parent = frame_001_2
    math_010_1.parent = frame_001_2
    math_011.parent = frame_001_2
    mix.parent = frame_019
    math_007_1.parent = frame_014
    reroute_002_2.parent = frame_016
    reroute_015_1.parent = frame_006
    group_002_1.parent = frame_015
    group_003_1.parent = frame_019
    group_004_1.parent = frame_014
    group_005_1.parent = frame_014
    reroute_016.parent = frame_016
    group_001_1.parent = frame_011
    distribute_points_on_faces.parent = frame_010
    repeat_input.parent = frame_011
    repeat_output.parent = frame_011
    math_004_2.parent = frame_011
    domain_size.parent = frame_010
    join_geometry_001.parent = frame_011
    join_geometry.parent = frame_011
    sample_index.parent = frame_011
    position_1.parent = frame_011
    transform_geometry_003_1.parent = frame_011
    group_006_1.parent = frame_011
    float_to_integer_002.parent = frame_011
    math_005_2.parent = frame_011
    reroute_018_1.parent = frame_011
    reroute_019_1.parent = frame_011
    group_007_1.parent = frame_011
    float_curve_001.parent = frame_018
    delete_geometry_1.parent = frame_010
    position_001_1.parent = frame_010
    compare_001_1.parent = frame_010
    separate_xyz_002_1.parent = frame_010
    compare_002.parent = frame_010
    math_008_1.parent = frame_010
    math_012.parent = frame_010
    boolean_math_1.parent = frame_010
    separate_xyz_003_1.parent = frame_010
    math_013.parent = frame_010
    math_014.parent = frame_010
    vector_math_1.parent = frame_011
    frame_010.parent = frame_011
    frame_012.parent = frame_016
    frame_013.parent = frame_016
    frame_014.parent = frame_016
    frame_015.parent = frame_016
    math_016.parent = frame_015
    position_006.parent = frame_012
    math_017.parent = frame_012
    vector_math_001_1.parent = frame_012
    math_018.parent = frame_012
    math_019.parent = frame_012
    set_position_1.parent = frame_014
    math_020.parent = frame_014
    math_021.parent = frame_014
    compare_003.parent = frame_014
    group_008_1.parent = frame_013
    math_022.parent = frame_013
    group_009_1.parent = frame_013
    distribute_points_on_faces_001.parent = frame_015
    random_value_1.parent = frame_015
    sample_index_001.parent = frame_012
    sample_nearest.parent = frame_012
    sample_index_002.parent = frame_015
    sample_nearest_001.parent = frame_015
    mix_001.parent = frame_014
    combine_xyz_003.parent = frame_012
    separate_xyz_004.parent = frame_012
    combine_xyz_004.parent = frame_012
    separate_xyz_005.parent = frame_012
    math_023.parent = frame_015
    vector_math_003_1.parent = frame_014
    sample_index_003.parent = frame_015
    string.parent = frame_015
    reroute_017_1.parent = frame_012
    reroute_020_1.parent = frame_012
    reroute_021_1.parent = frame_016
    reroute_022_1.parent = frame_014
    reroute_023.parent = frame_016
    store_named_attribute.parent = frame_015
    store_named_attribute_001.parent = frame_015
    named_attribute.parent = frame_015
    named_attribute_001.parent = frame_015
    string_001.parent = frame_015
    float_curve_002.parent = frame_009
    reroute_025.parent = frame_013
    reroute_026.parent = frame_013
    position_007.parent = frame_014
    vector_math_004_1.parent = frame_014
    reroute_027.parent = frame_013
    math_024.parent = frame_014
    math_025.parent = frame_014
    reroute_028.parent = frame_016
    reroute_033.parent = frame_010
    reroute_032.parent = frame_010
    reroute_029.parent = frame_016
    reroute_030.parent = frame_016
    frame_009.parent = frame_015
    frame_018.parent = frame_011
    reroute_024.parent = frame_016
    frame_019.parent = frame_016
    reroute_035.parent = frame_014
    boolean_math_001.parent = frame_010
    combine_xyz_005.parent = frame_010
    vector_math_005.parent = frame_010
    compare_004.parent = frame_010
    mix_002.parent = frame_020
    math_026.parent = frame_020
    group_010_1.parent = frame_020
    math_027.parent = frame_020
    frame_020.parent = frame_010
    math_028.parent = frame_010
    group_011_1.parent = frame_010
    reroute_036.parent = frame_020
    math_029.parent = frame_011
    attribute_statistic_1.parent = frame_011
    position_008.parent = frame_011
    separate_xyz_006.parent = frame_011
    combine_xyz_006.parent = frame_011
    transform_geometry_004.parent = frame_011
    vector_math_006.parent = frame_011
    group_012_1.parent = frame_011
    math_015.parent = frame_011
    math_030.parent = frame_011
    float_to_integer_001.parent = frame_011
    mesh_boolean_1.parent = frame_011
    switch_2.parent = frame_011
    reroute_037.parent = frame_011
    value.parent = frame_020

    # Set locations
    group_input_4.location = (-20139.841796875, -110.3683853149414)
    group_output_4.location = (2688.79150390625, 0.0)
    grid.location = (-3688.64208984375, 698.6746215820312)
    set_material_1.location = (2465.73583984375, 28.000001907348633)
    set_shade_smooth_1.location = (2275.73583984375, 40.0)
    vector_math_012.location = (1723.7470703125, 52.151824951171875)
    raycast.location = (1523.7470703125, 52.1068115234375)
    frame_002_1.location = (-19502.08203125, -285.6419982910156)
    vector_math_017.location = (1293.6964111328125, -877.6812133789062)
    gradient_texture_001.location = (623.6964111328125, -966.2945556640625)
    position_002_1.location = (243.6964111328125, -887.7945556640625)
    vector_math_019.location = (433.6964111328125, -964.2945556640625)
    set_position_001_1.location = (1483.6964111328125, -588.5987548828125)
    position_003.location = (1103.6964111328125, -902.2945556640625)
    combine_xyz_1.location = (1103.6964111328125, -967.2945556640625)
    math_3.location = (243.6964111328125, -952.7945556640625)
    frame_2.location = (449.989990234375, 577.474853515625)
    reroute_001_1.location = (1091.744873046875, 84.72909545898438)
    vector_math_002_1.location = (-5025.19091796875, 679.6746215820312)
    vector_math_021.location = (-4835.19091796875, 668.6746215820312)
    separate_xyz_1.location = (-4455.19091796875, 676.6746215820312)
    vector_math_023.location = (-4645.19091796875, 709.6746215820312)
    frame_001_2.location = (-17219.966796875, -823.490966796875)
    reroute_003_2.location = (183.4259033203125, -785.5428466796875)
    compare_1.location = (1293.6964111328125, -694.6812133789062)
    math_001_3.location = (-19907.025390625, -346.03912353515625)
    integer_012.location = (-20097.025390625, -425.69342041015625)
    reroute_005_1.location = (-19012.7734375, 629.6964111328125)
    float_to_integer_1.location = (-19717.025390625, -370.53912353515625)
    transform_geometry_001_1.location = (1809.3837890625, -34.2188835144043)
    attribute_statistic_001.location = (1429.3837890625, -261.3872375488281)
    position_004_1.location = (1239.3837890625, -356.2337951660156)
    reroute_007.location = (1271.6622314453125, -105.46165466308594)
    vector_math_028.location = (1619.3837890625, -188.43307495117188)
    frame_003_2.location = (-18598.47265625, -89.21844482421875)
    reroute_008.location = (-14253.6787109375, 629.6964111328125)
    reroute_006_1.location = (633.416015625, 491.5299987792969)
    reroute_004_1.location = (-19012.7734375, 547.1276245117188)
    noise_texture_009.location = (-5233.6884765625, -202.95066833496094)
    group_013_1.location = (-5423.6884765625, 128.54934692382812)
    reroute_009.location = (-5485.20556640625, -395.0369873046875)
    group_2.location = (-5423.6884765625, -49.450653076171875)
    group_014_1.location = (-5423.6884765625, -249.45065307617188)
    group_015.location = (-5423.6884765625, -449.4506530761719)
    group_016.location = (-5423.6884765625, -649.45068359375)
    frame_004_1.location = (-549.12451171875, 255.1417236328125)
    noise_texture_010.location = (-5233.6884765625, 35.4810791015625)
    group_017.location = (-5423.6884765625, 238.87225341796875)
    reroute_010_1.location = (-5485.20556640625, -156.605224609375)
    group_018.location = (-5423.6884765625, 60.87225341796875)
    group_020.location = (-5423.6884765625, -139.12774658203125)
    group_021.location = (-5423.6884765625, -339.12774658203125)
    frame_005_1.location = (-549.12451171875, -904.7757568359375)
    noise_texture_011_1.location = (-5233.6884765625, 35.4810791015625)
    group_019_1.location = (-5423.6884765625, 236.93341064453125)
    reroute_011.location = (-5485.20556640625, -156.605224609375)
    group_022_1.location = (-5423.6884765625, 58.93341064453125)
    group_023_1.location = (-5423.6884765625, -141.06658935546875)
    group_024_1.location = (-5423.6884765625, -341.06658935546875)
    frame_006.location = (-549.12451171875, -2146.79296875)
    group_026.location = (-5423.6884765625, -539.1277465820312)
    set_position_005.location = (-5050.517578125, 510.89593505859375)
    math_002_2.location = (-5043.6884765625, -267.95068359375)
    math_003_2.location = (-5043.6884765625, -40.5189208984375)
    combine_xyz_002.location = (-5240.517578125, 417.0015869140625)
    vector.location = (1343.6845703125, -151.84811401367188)
    transform_geometry_1.location = (1913.7470703125, 160.67318725585938)
    float_curve_1.location = (823.550048828125, -862.5306396484375)
    reroute_1.location = (1271.14111328125, -50.05318832397461)
    frame_007.location = (-14472.8359375, -634.546142578125)
    reroute_012_1.location = (-6169.27001953125, -1060.4754638671875)
    transform_geometry_002_1.location = (1809.3837890625, -34.2188835144043)
    attribute_statistic_002.location = (1429.3837890625, -261.3872375488281)
    position_005.location = (1239.3837890625, -356.2337951660156)
    reroute_013_1.location = (1269.0, -74.0)
    vector_math_030.location = (1619.3837890625, -188.43307495117188)
    frame_008.location = (-20460.8359375, -89.54608154296875)
    separate_xyz_001_1.location = (-12082.7216796875, -14.499267578125)
    math_006_1.location = (-11626.6884765625, 19.28466796875)
    math_009.location = (-4126.19921875, 820.5626220703125)
    math_010_1.location = (-3936.19921875, 943.5841064453125)
    math_011.location = (-3936.19921875, 780.5841064453125)
    mix.location = (-11892.7216796875, 11.000732421875)
    math_007_1.location = (2495.16748046875, -107.586181640625)
    reroute_002_2.location = (-12353.2109375, 603.22412109375)
    reroute_014.location = (-19012.7734375, 455.10919189453125)
    reroute_015_1.location = (-5028.4130859375, -0.2525634765625)
    group_002_1.location = (-1929.091796875, 647.364501953125)
    group_003_1.location = (-11892.7216796875, -153.999267578125)
    group_004_1.location = (2187.833984375, -187.9140625)
    group_005_1.location = (2333.65234375, -481.912841796875)
    reroute_016.location = (-5319.115234375, 507.653076171875)
    group_001_1.location = (-819.889404296875, -1910.8944091796875)
    distribute_points_on_faces.location = (-3653.6591796875, -1898.399169921875)
    repeat_input.location = (-2826.2900390625, -1771.716796875)
    repeat_output.location = (538.6717529296875, -1682.5692138671875)
    math_004_2.location = (-2622.460693359375, -1839.3734130859375)
    domain_size.location = (-2693.789794921875, -1445.665771484375)
    join_geometry_001.location = (350.13262939453125, -1712.322998046875)
    join_geometry.location = (719.3307495117188, -1364.4150390625)
    sample_index.location = (-1012.987060546875, -1539.5640869140625)
    position_1.location = (-1249.7659912109375, -1682.3516845703125)
    transform_geometry_003_1.location = (181.31292724609375, -1813.9224853515625)
    group_006_1.location = (-2622.460693359375, -2002.3734130859375)
    float_to_integer_002.location = (-2431.11474609375, -2116.7001953125)
    math_005_2.location = (-2257.52294921875, -2077.4814453125)
    reroute_018_1.location = (-1411.2899169921875, -1857.4189453125)
    reroute_019_1.location = (-2063.73583984375, -2188.722412109375)
    group_007_1.location = (-2035.07275390625, -2228.327880859375)
    float_curve_001.location = (-1372.047119140625, -2293.55224609375)
    delete_geometry_1.location = (-2879.869384765625, -1799.16943359375)
    position_001_1.location = (-4157.068359375, -1436.1982421875)
    compare_001_1.location = (-3443.21533203125, -1393.573486328125)
    separate_xyz_002_1.location = (-3988.1025390625, -1381.181640625)
    compare_002.location = (-3443.21533203125, -1556.573486328125)
    math_008_1.location = (-3635.16259765625, -1406.525146484375)
    math_012.location = (-3635.16259765625, -1265.525146484375)
    boolean_math_1.location = (-3274.486328125, -1445.961181640625)
    separate_xyz_003_1.location = (-4400.02490234375, -1621.657470703125)
    math_013.location = (-3635.16259765625, -1547.525146484375)
    math_014.location = (-3635.16259765625, -1710.525146484375)
    vector_math_1.location = (-16.22247314453125, -1776.3204345703125)
    frame_010.location = (-341.00390625, -319.9088134765625)
    frame_011.location = (-531.6533203125, 1641.8719482421875)
    frame_012.location = (-8167.3359375, -548.3059692382812)
    frame_013.location = (-8267.5791015625, -530.7792358398438)
    frame_014.location = (-8980.685546875, -411.666748046875)
    frame_015.location = (-9216.7783203125, -706.154541015625)
    math_016.location = (-1929.228515625, 811.864990234375)
    position_006.location = (-908.1362915039062, -275.6748046875)
    math_017.location = (6.1168670654296875, -261.18353271484375)
    vector_math_001_1.location = (6.1168670654296875, -123.18353271484375)
    math_018.location = (222.644775390625, -51.94435119628906)
    math_019.location = (435.18646240234375, -276.8241271972656)
    set_position_1.location = (3694.345703125, 720.9320068359375)
    math_020.location = (2582.36279296875, -366.502197265625)
    math_021.location = (2766.23486328125, -300.075927734375)
    compare_003.location = (2956.23486328125, -148.575927734375)
    group_008_1.location = (872.8798828125, -219.51327514648438)
    math_022.location = (1104.73193359375, -328.0132751464844)
    group_009_1.location = (878.6954956054688, -402.7296142578125)
    distribute_points_on_faces_001.location = (-1553.310546875, 911.906494140625)
    random_value_1.location = (-1399.2080078125, 504.205078125)
    sample_index_001.location = (-576.4902954101562, -264.4415283203125)
    sample_nearest.location = (-908.1362915039062, -139.67478942871094)
    sample_index_002.location = (-196.78634643554688, 490.788818359375)
    sample_nearest_001.location = (-196.78634643554688, 282.788818359375)
    mix_001.location = (2766.23486328125, -463.075927734375)
    combine_xyz_003.location = (-195.4925537109375, -102.58157348632812)
    separate_xyz_004.location = (-385.4925537109375, -102.58157348632812)
    combine_xyz_004.location = (-195.4925537109375, -216.58157348632812)
    separate_xyz_005.location = (-385.4925537109375, -216.58157348632812)
    math_023.location = (-1613.025390625, 500.482666015625)
    vector_math_003_1.location = (2957.271484375, -329.651611328125)
    sample_index_003.location = (-196.78634643554688, 698.788818359375)
    string.location = (-766.786376953125, 641.788818359375)
    reroute_017_1.location = (-958.184814453125, -57.933448791503906)
    reroute_020_1.location = (-671.9747314453125, -63.218414306640625)
    reroute_021_1.location = (-8019.77734375, -315.61285400390625)
    reroute_022_1.location = (2671.4296875, 329.2344970703125)
    reroute_023.location = (-6974.6123046875, -337.19195556640625)
    store_named_attribute.location = (-576.786376953125, 697.288818359375)
    store_named_attribute_001.location = (-576.786376953125, 489.288818359375)
    named_attribute.location = (-386.786376953125, 454.788818359375)
    named_attribute_001.location = (-386.786376953125, 662.788818359375)
    string_001.location = (-766.786376953125, 433.788818359375)
    float_curve_002.location = (-1177.958984375, 551.424072265625)
    reroute_025.location = (815.8261108398438, -352.51995849609375)
    reroute_026.location = (815.8261108398438, -404.6067810058594)
    position_007.location = (3121.39794921875, -235.381591796875)
    vector_math_004_1.location = (3292.11669921875, -324.158935546875)
    reroute_027.location = (815.8261108398438, -459.7581481933594)
    math_024.location = (2592.224609375, -553.886962890625)
    math_025.location = (2122.2080078125, -639.906982421875)
    frame_016.location = (-392.5830078125, -138.754150390625)
    frame_017.location = (3337.47265625, 39.33642578125)
    reroute_028.location = (-12313.919921875, 232.63449096679688)
    reroute_031.location = (-4957.95703125, 105.62429809570312)
    reroute_033.location = (-3918.189453125, -936.4093627929688)
    reroute_032.location = (-4368.0498046875, -951.0938720703125)
    reroute_029.location = (-10929.2783203125, 576.5614013671875)
    reroute_030.location = (-7592.81689453125, 535.5804443359375)
    frame_009.location = (0.0, 0.0)
    frame_018.location = (-436.04638671875, -65.78271484375)
    reroute_024.location = (-8356.40625, 81.64697265625)
    frame_019.location = (0.0, 0.0)
    reroute_035.location = (2423.4267578125, 451.5533447265625)
    boolean_math_001.location = (-3093.355712890625, -1361.449951171875)
    combine_xyz_005.location = (-3639.12841796875, -1051.4248046875)
    vector_math_005.location = (-3448.10986328125, -1047.768310546875)
    compare_004.location = (-3235.63427734375, -1000.1389770507812)
    reroute_034.location = (-4273.96142578125, 492.3140563964844)
    mix_002.location = (-4238.23583984375, -1766.8883056640625)
    math_026.location = (-4076.0029296875, -1815.3262939453125)
    group_010_1.location = (-4249.86669921875, -1967.1490478515625)
    math_027.location = (-3915.177734375, -1962.415283203125)
    frame_020.location = (-90.3408203125, -2.58349609375)
    math_028.location = (-3836.5595703125, -2019.7752685546875)
    group_011_1.location = (-3877.59326171875, -1768.8453369140625)
    reroute_036.location = (-3849.791015625, -1913.984619140625)
    math_029.location = (-1449.9278564453125, -2302.19384765625)
    attribute_statistic_1.location = (-820.4967041015625, -1737.9093017578125)
    position_008.location = (-994.4837646484375, -1818.0142822265625)
    separate_xyz_006.location = (-626.9385986328125, -1786.962646484375)
    combine_xyz_006.location = (-456.7769775390625, -1812.57177734375)
    transform_geometry_004.location = (-70.228759765625, -2040.658935546875)
    vector_math_006.location = (-241.3167724609375, -1806.5072021484375)
    group_012_1.location = (-624.1229248046875, -1904.078857421875)
    math_015.location = (-1343.6787109375, -2083.6689453125)
    reroute_040.location = (-19012.7734375, 510.05523681640625)
    reroute_038.location = (-2611.3583984375, 618.0911865234375)
    math_030.location = (-1180.303955078125, -2087.87548828125)
    float_to_integer_001.location = (-993.7366943359375, -2032.217529296875)
    mesh_boolean_1.location = (728.8812255859375, -1529.47021484375)
    switch_2.location = (926.2166748046875, -1416.4339599609375)
    reroute_037.location = (561.221435546875, -1418.1854248046875)
    reroute_039.location = (-19012.7734375, 690.58740234375)
    reroute_041.location = (264.3801574707031, 689.6874389648438)
    value.location = (-4086.73583984375, -2041.174560546875)

    # initialize martianterrain links
    # set_material_1.Geometry -> group_output_4.Geometry
    martianterrain.links.new(set_material_1.outputs[0], group_output_4.inputs[0])
    # set_shade_smooth_1.Geometry -> set_material_1.Geometry
    martianterrain.links.new(set_shade_smooth_1.outputs[0], set_material_1.inputs[0])
    # reroute_001_1.Output -> raycast.Target Geometry
    martianterrain.links.new(reroute_001_1.outputs[0], raycast.inputs[0])
    # raycast.Hit Position -> vector_math_012.Vector
    martianterrain.links.new(raycast.outputs[1], vector_math_012.inputs[0])
    # vector_math_019.Vector -> gradient_texture_001.Vector
    martianterrain.links.new(vector_math_019.outputs[0], gradient_texture_001.inputs[0])
    # position_002_1.Position -> vector_math_019.Vector
    martianterrain.links.new(position_002_1.outputs[0], vector_math_019.inputs[0])
    # combine_xyz_1.Vector -> vector_math_017.Vector
    martianterrain.links.new(combine_xyz_1.outputs[0], vector_math_017.inputs[1])
    # position_003.Position -> vector_math_017.Vector
    martianterrain.links.new(position_003.outputs[0], vector_math_017.inputs[0])
    # float_curve_1.Value -> combine_xyz_1.Z
    martianterrain.links.new(float_curve_1.outputs[0], combine_xyz_1.inputs[2])
    # group_input_4.Scale -> vector_math_002_1.Vector
    martianterrain.links.new(group_input_4.outputs[1], vector_math_002_1.inputs[0])
    # group_input_4.Density -> vector_math_002_1.Vector
    martianterrain.links.new(group_input_4.outputs[2], vector_math_002_1.inputs[1])
    # vector_math_002_1.Vector -> vector_math_021.Vector
    martianterrain.links.new(vector_math_002_1.outputs[0], vector_math_021.inputs[0])
    # separate_xyz_1.X -> grid.Vertices X
    martianterrain.links.new(separate_xyz_1.outputs[0], grid.inputs[2])
    # separate_xyz_1.Y -> grid.Vertices Y
    martianterrain.links.new(separate_xyz_1.outputs[1], grid.inputs[3])
    # vector_math_021.Vector -> vector_math_023.Vector
    martianterrain.links.new(vector_math_021.outputs[0], vector_math_023.inputs[0])
    # vector_math_023.Vector -> separate_xyz_1.Vector
    martianterrain.links.new(vector_math_023.outputs[0], separate_xyz_1.inputs[0])
    # reroute_003_2.Output -> math_3.Value
    martianterrain.links.new(reroute_003_2.outputs[0], math_3.inputs[0])
    # reroute_006_1.Output -> reroute_003_2.Input
    martianterrain.links.new(reroute_006_1.outputs[0], reroute_003_2.inputs[0])
    # reroute_003_2.Output -> compare_1.A
    martianterrain.links.new(reroute_003_2.outputs[0], compare_1.inputs[0])
    # compare_1.Result -> set_position_001_1.Selection
    martianterrain.links.new(compare_1.outputs[0], set_position_001_1.inputs[1])
    # integer_012.Integer -> math_001_3.Value
    martianterrain.links.new(integer_012.outputs[0], math_001_3.inputs[1])
    # group_input_4.Seed -> math_001_3.Value
    martianterrain.links.new(group_input_4.outputs[0], math_001_3.inputs[0])
    # group_input_4.Scale -> reroute_005_1.Input
    martianterrain.links.new(group_input_4.outputs[1], reroute_005_1.inputs[0])
    # math_001_3.Value -> float_to_integer_1.Float
    martianterrain.links.new(math_001_3.outputs[0], float_to_integer_1.inputs[0])
    # position_004_1.Position -> attribute_statistic_001.Attribute
    martianterrain.links.new(
        position_004_1.outputs[0], attribute_statistic_001.inputs[2]
    )
    # reroute_007.Output -> attribute_statistic_001.Geometry
    martianterrain.links.new(reroute_007.outputs[0], attribute_statistic_001.inputs[0])
    # vector_math_028.Vector -> transform_geometry_001_1.Scale
    martianterrain.links.new(
        vector_math_028.outputs[0], transform_geometry_001_1.inputs[3]
    )
    # attribute_statistic_001.Range -> vector_math_028.Vector
    martianterrain.links.new(
        attribute_statistic_001.outputs[5], vector_math_028.inputs[1]
    )
    # reroute_1.Output -> vector_math_028.Vector
    martianterrain.links.new(reroute_1.outputs[0], vector_math_028.inputs[0])
    # reroute_005_1.Output -> reroute_008.Input
    martianterrain.links.new(reroute_005_1.outputs[0], reroute_008.inputs[0])
    # reroute_034.Output -> reroute_006_1.Input
    martianterrain.links.new(reroute_034.outputs[0], reroute_006_1.inputs[0])
    # group_input_4.Flat Area Size -> reroute_004_1.Input
    martianterrain.links.new(group_input_4.outputs[3], reroute_004_1.inputs[0])
    # group_013_1.Value -> noise_texture_009.W
    martianterrain.links.new(group_013_1.outputs[0], noise_texture_009.inputs[1])
    # reroute_012_1.Output -> reroute_009.Input
    martianterrain.links.new(reroute_012_1.outputs[0], reroute_009.inputs[0])
    # reroute_009.Output -> group_013_1.Seed
    martianterrain.links.new(reroute_009.outputs[0], group_013_1.inputs[2])
    # reroute_009.Output -> group_2.Seed
    martianterrain.links.new(reroute_009.outputs[0], group_2.inputs[3])
    # group_2.Value -> noise_texture_009.Scale
    martianterrain.links.new(group_2.outputs[0], noise_texture_009.inputs[2])
    # reroute_009.Output -> group_014_1.Seed
    martianterrain.links.new(reroute_009.outputs[0], group_014_1.inputs[3])
    # group_014_1.Value -> noise_texture_009.Detail
    martianterrain.links.new(group_014_1.outputs[0], noise_texture_009.inputs[3])
    # reroute_009.Output -> group_015.Seed
    martianterrain.links.new(reroute_009.outputs[0], group_015.inputs[3])
    # group_015.Value -> noise_texture_009.Roughness
    martianterrain.links.new(group_015.outputs[0], noise_texture_009.inputs[4])
    # reroute_009.Output -> group_016.Seed
    martianterrain.links.new(reroute_009.outputs[0], group_016.inputs[3])
    # group_016.Value -> noise_texture_009.Lacunarity
    martianterrain.links.new(group_016.outputs[0], noise_texture_009.inputs[5])
    # group_017.Value -> noise_texture_010.W
    martianterrain.links.new(group_017.outputs[0], noise_texture_010.inputs[1])
    # reroute_010_1.Output -> group_017.Seed
    martianterrain.links.new(reroute_010_1.outputs[0], group_017.inputs[2])
    # reroute_010_1.Output -> group_018.Seed
    martianterrain.links.new(reroute_010_1.outputs[0], group_018.inputs[3])
    # group_018.Value -> noise_texture_010.Scale
    martianterrain.links.new(group_018.outputs[0], noise_texture_010.inputs[2])
    # reroute_010_1.Output -> group_020.Seed
    martianterrain.links.new(reroute_010_1.outputs[0], group_020.inputs[3])
    # group_020.Value -> noise_texture_010.Roughness
    martianterrain.links.new(group_020.outputs[0], noise_texture_010.inputs[4])
    # reroute_010_1.Output -> group_021.Seed
    martianterrain.links.new(reroute_010_1.outputs[0], group_021.inputs[3])
    # group_021.Value -> noise_texture_010.Lacunarity
    martianterrain.links.new(group_021.outputs[0], noise_texture_010.inputs[5])
    # reroute_012_1.Output -> reroute_010_1.Input
    martianterrain.links.new(reroute_012_1.outputs[0], reroute_010_1.inputs[0])
    # group_019_1.Value -> noise_texture_011_1.W
    martianterrain.links.new(group_019_1.outputs[0], noise_texture_011_1.inputs[1])
    # reroute_011.Output -> group_019_1.Seed
    martianterrain.links.new(reroute_011.outputs[0], group_019_1.inputs[2])
    # reroute_011.Output -> group_022_1.Seed
    martianterrain.links.new(reroute_011.outputs[0], group_022_1.inputs[3])
    # group_022_1.Value -> noise_texture_011_1.Scale
    martianterrain.links.new(group_022_1.outputs[0], noise_texture_011_1.inputs[2])
    # reroute_011.Output -> group_023_1.Seed
    martianterrain.links.new(reroute_011.outputs[0], group_023_1.inputs[3])
    # group_023_1.Value -> noise_texture_011_1.Roughness
    martianterrain.links.new(group_023_1.outputs[0], noise_texture_011_1.inputs[4])
    # reroute_011.Output -> group_024_1.Seed
    martianterrain.links.new(reroute_011.outputs[0], group_024_1.inputs[3])
    # group_024_1.Value -> noise_texture_011_1.Lacunarity
    martianterrain.links.new(group_024_1.outputs[0], noise_texture_011_1.inputs[5])
    # reroute_012_1.Output -> reroute_011.Input
    martianterrain.links.new(reroute_012_1.outputs[0], reroute_011.inputs[0])
    # reroute_010_1.Output -> group_026.Seed
    martianterrain.links.new(reroute_010_1.outputs[0], group_026.inputs[3])
    # group_026.Value -> noise_texture_010.Offset
    martianterrain.links.new(group_026.outputs[0], noise_texture_010.inputs[6])
    # grid.Mesh -> set_position_005.Geometry
    martianterrain.links.new(grid.outputs[0], set_position_005.inputs[0])
    # noise_texture_009.Fac -> math_002_2.Value
    martianterrain.links.new(noise_texture_009.outputs[0], math_002_2.inputs[0])
    # noise_texture_010.Fac -> math_003_2.Value
    martianterrain.links.new(noise_texture_010.outputs[0], math_003_2.inputs[0])
    # reroute_015_1.Output -> math_003_2.Value
    martianterrain.links.new(reroute_015_1.outputs[0], math_003_2.inputs[1])
    # math_003_2.Value -> math_002_2.Value
    martianterrain.links.new(math_003_2.outputs[0], math_002_2.inputs[1])
    # math_002_2.Value -> combine_xyz_002.Z
    martianterrain.links.new(math_002_2.outputs[0], combine_xyz_002.inputs[2])
    # combine_xyz_002.Vector -> set_position_005.Offset
    martianterrain.links.new(combine_xyz_002.outputs[0], set_position_005.inputs[3])
    # vector.Vector -> raycast.Source Position
    martianterrain.links.new(vector.outputs[0], raycast.inputs[2])
    # reroute_007.Output -> transform_geometry_001_1.Geometry
    martianterrain.links.new(reroute_007.outputs[0], transform_geometry_001_1.inputs[0])
    # vector_math_012.Vector -> transform_geometry_1.Translation
    martianterrain.links.new(vector_math_012.outputs[0], transform_geometry_1.inputs[1])
    # reroute_001_1.Output -> transform_geometry_1.Geometry
    martianterrain.links.new(reroute_001_1.outputs[0], transform_geometry_1.inputs[0])
    # vector_math_017.Vector -> set_position_001_1.Position
    martianterrain.links.new(vector_math_017.outputs[0], set_position_001_1.inputs[2])
    # gradient_texture_001.Fac -> float_curve_1.Value
    martianterrain.links.new(gradient_texture_001.outputs[1], float_curve_1.inputs[1])
    # math_3.Value -> vector_math_019.Vector
    martianterrain.links.new(math_3.outputs[0], vector_math_019.inputs[1])
    # reroute_008.Output -> reroute_1.Input
    martianterrain.links.new(reroute_008.outputs[0], reroute_1.inputs[0])
    # float_to_integer_1.Integer -> reroute_012_1.Input
    martianterrain.links.new(float_to_integer_1.outputs[0], reroute_012_1.inputs[0])
    # position_005.Position -> attribute_statistic_002.Attribute
    martianterrain.links.new(position_005.outputs[0], attribute_statistic_002.inputs[2])
    # reroute_013_1.Output -> attribute_statistic_002.Geometry
    martianterrain.links.new(
        reroute_013_1.outputs[0], attribute_statistic_002.inputs[0]
    )
    # vector_math_030.Vector -> transform_geometry_002_1.Scale
    martianterrain.links.new(
        vector_math_030.outputs[0], transform_geometry_002_1.inputs[3]
    )
    # attribute_statistic_002.Range -> vector_math_030.Vector
    martianterrain.links.new(
        attribute_statistic_002.outputs[5], vector_math_030.inputs[1]
    )
    # reroute_013_1.Output -> transform_geometry_002_1.Geometry
    martianterrain.links.new(
        reroute_013_1.outputs[0], transform_geometry_002_1.inputs[0]
    )
    # set_position_005.Geometry -> reroute_013_1.Input
    martianterrain.links.new(set_position_005.outputs[0], reroute_013_1.inputs[0])
    # transform_geometry_002_1.Geometry -> reroute_001_1.Input
    martianterrain.links.new(
        transform_geometry_002_1.outputs[0], reroute_001_1.inputs[0]
    )
    # transform_geometry_1.Geometry -> reroute_007.Input
    martianterrain.links.new(transform_geometry_1.outputs[0], reroute_007.inputs[0])
    # reroute_008.Output -> separate_xyz_001_1.Vector
    martianterrain.links.new(reroute_008.outputs[0], separate_xyz_001_1.inputs[0])
    # separate_xyz_1.X -> math_009.Value
    martianterrain.links.new(separate_xyz_1.outputs[0], math_009.inputs[0])
    # separate_xyz_1.Y -> math_009.Value
    martianterrain.links.new(separate_xyz_1.outputs[1], math_009.inputs[1])
    # separate_xyz_1.X -> math_010_1.Value
    martianterrain.links.new(separate_xyz_1.outputs[0], math_010_1.inputs[0])
    # math_009.Value -> math_010_1.Value
    martianterrain.links.new(math_009.outputs[0], math_010_1.inputs[1])
    # math_009.Value -> math_011.Value
    martianterrain.links.new(math_009.outputs[0], math_011.inputs[1])
    # separate_xyz_1.Y -> math_011.Value
    martianterrain.links.new(separate_xyz_1.outputs[1], math_011.inputs[0])
    # math_010_1.Value -> grid.Size X
    martianterrain.links.new(math_010_1.outputs[0], grid.inputs[0])
    # math_011.Value -> grid.Size Y
    martianterrain.links.new(math_011.outputs[0], grid.inputs[1])
    # separate_xyz_001_1.X -> mix.A
    martianterrain.links.new(separate_xyz_001_1.outputs[0], mix.inputs[2])
    # separate_xyz_001_1.Y -> mix.B
    martianterrain.links.new(separate_xyz_001_1.outputs[1], mix.inputs[3])
    # mix.Result -> math_006_1.Value
    martianterrain.links.new(mix.outputs[0], math_006_1.inputs[0])
    # reroute_035.Output -> math_007_1.Value
    martianterrain.links.new(reroute_035.outputs[0], math_007_1.inputs[0])
    # reroute_014.Output -> reroute_002_2.Input
    martianterrain.links.new(reroute_014.outputs[0], reroute_002_2.inputs[0])
    # float_to_integer_1.Integer -> reroute_014.Input
    martianterrain.links.new(float_to_integer_1.outputs[0], reroute_014.inputs[0])
    # noise_texture_011_1.Fac -> reroute_015_1.Input
    martianterrain.links.new(noise_texture_011_1.outputs[0], reroute_015_1.inputs[0])
    # reroute_002_2.Output -> group_002_1.Seed
    martianterrain.links.new(reroute_002_2.outputs[0], group_002_1.inputs[3])
    # reroute_002_2.Output -> group_003_1.Seed
    martianterrain.links.new(reroute_002_2.outputs[0], group_003_1.inputs[3])
    # group_003_1.Value -> math_006_1.Value
    martianterrain.links.new(group_003_1.outputs[0], math_006_1.inputs[1])
    # reroute_002_2.Output -> group_004_1.Seed
    martianterrain.links.new(reroute_002_2.outputs[0], group_004_1.inputs[3])
    # group_004_1.Value -> math_007_1.Value
    martianterrain.links.new(group_004_1.outputs[0], math_007_1.inputs[1])
    # reroute_002_2.Output -> group_005_1.Seed
    martianterrain.links.new(reroute_002_2.outputs[0], group_005_1.inputs[3])
    # set_position_001_1.Geometry -> set_shade_smooth_1.Geometry
    martianterrain.links.new(
        set_position_001_1.outputs[0], set_shade_smooth_1.inputs[0]
    )
    # compare_001_1.Result -> boolean_math_1.Boolean
    martianterrain.links.new(compare_001_1.outputs[0], boolean_math_1.inputs[0])
    # compare_002.Result -> boolean_math_1.Boolean
    martianterrain.links.new(compare_002.outputs[0], boolean_math_1.inputs[1])
    # group_006_1.Value -> float_to_integer_002.Float
    martianterrain.links.new(group_006_1.outputs[0], float_to_integer_002.inputs[0])
    # math_013.Value -> compare_001_1.B
    martianterrain.links.new(math_013.outputs[0], compare_001_1.inputs[1])
    # float_to_integer_002.Integer -> math_005_2.Value
    martianterrain.links.new(float_to_integer_002.outputs[0], math_005_2.inputs[1])
    # repeat_output.Geometry -> join_geometry.Geometry
    martianterrain.links.new(repeat_output.outputs[0], join_geometry.inputs[0])
    # separate_xyz_003_1.X -> math_013.Value
    martianterrain.links.new(separate_xyz_003_1.outputs[0], math_013.inputs[0])
    # delete_geometry_1.Geometry -> sample_index.Geometry
    martianterrain.links.new(delete_geometry_1.outputs[0], sample_index.inputs[0])
    # separate_xyz_003_1.Y -> math_014.Value
    martianterrain.links.new(separate_xyz_003_1.outputs[1], math_014.inputs[0])
    # math_004_2.Value -> reroute_018_1.Input
    martianterrain.links.new(math_004_2.outputs[0], reroute_018_1.inputs[0])
    # math_014.Value -> compare_002.B
    martianterrain.links.new(math_014.outputs[0], compare_002.inputs[1])
    # math_005_2.Value -> reroute_019_1.Input
    martianterrain.links.new(math_005_2.outputs[0], reroute_019_1.inputs[0])
    # math_008_1.Value -> compare_002.A
    martianterrain.links.new(math_008_1.outputs[0], compare_002.inputs[0])
    # math_004_2.Value -> math_005_2.Value
    martianterrain.links.new(math_004_2.outputs[0], math_005_2.inputs[0])
    # repeat_input.Point Index -> math_004_2.Value
    martianterrain.links.new(repeat_input.outputs[1], math_004_2.inputs[0])
    # reroute_019_1.Output -> group_007_1.Seed
    martianterrain.links.new(reroute_019_1.outputs[0], group_007_1.inputs[2])
    # reroute_019_1.Output -> group_001_1.Seed
    martianterrain.links.new(reroute_019_1.outputs[0], group_001_1.inputs[0])
    # delete_geometry_1.Geometry -> domain_size.Geometry
    martianterrain.links.new(delete_geometry_1.outputs[0], domain_size.inputs[0])
    # group_007_1.Value -> float_curve_001.Value
    martianterrain.links.new(group_007_1.outputs[0], float_curve_001.inputs[1])
    # distribute_points_on_faces.Points -> delete_geometry_1.Geometry
    martianterrain.links.new(
        distribute_points_on_faces.outputs[0], delete_geometry_1.inputs[0]
    )
    # join_geometry_001.Geometry -> repeat_output.Geometry
    martianterrain.links.new(join_geometry_001.outputs[0], repeat_output.inputs[0])
    # domain_size.Point Count -> repeat_input.Iterations
    martianterrain.links.new(domain_size.outputs[0], repeat_input.inputs[0])
    # position_001_1.Position -> separate_xyz_002_1.Vector
    martianterrain.links.new(position_001_1.outputs[0], separate_xyz_002_1.inputs[0])
    # reroute_018_1.Output -> repeat_output.Point Index
    martianterrain.links.new(reroute_018_1.outputs[0], repeat_output.inputs[1])
    # math_012.Value -> compare_001_1.A
    martianterrain.links.new(math_012.outputs[0], compare_001_1.inputs[0])
    # reroute_018_1.Output -> sample_index.Index
    martianterrain.links.new(reroute_018_1.outputs[0], sample_index.inputs[2])
    # position_1.Position -> sample_index.Value
    martianterrain.links.new(position_1.outputs[0], sample_index.inputs[1])
    # separate_xyz_002_1.X -> math_012.Value
    martianterrain.links.new(separate_xyz_002_1.outputs[0], math_012.inputs[0])
    # separate_xyz_002_1.Y -> math_008_1.Value
    martianterrain.links.new(separate_xyz_002_1.outputs[1], math_008_1.inputs[0])
    # repeat_input.Geometry -> join_geometry_001.Geometry
    martianterrain.links.new(repeat_input.outputs[0], join_geometry_001.inputs[0])
    # reroute_036.Output -> distribute_points_on_faces.Seed
    martianterrain.links.new(
        reroute_036.outputs[0], distribute_points_on_faces.inputs[6]
    )
    # reroute_031.Output -> group_006_1.Seed
    martianterrain.links.new(reroute_031.outputs[0], group_006_1.inputs[2])
    # reroute_032.Output -> separate_xyz_003_1.Vector
    martianterrain.links.new(reroute_032.outputs[0], separate_xyz_003_1.inputs[0])
    # switch_2.Output -> set_position_001_1.Geometry
    martianterrain.links.new(switch_2.outputs[0], set_position_001_1.inputs[0])
    # math_018.Value -> compare_003.A
    martianterrain.links.new(math_018.outputs[0], compare_003.inputs[0])
    # math_018.Value -> math_019.Value
    martianterrain.links.new(math_018.outputs[0], math_019.inputs[1])
    # math_019.Value -> group_008_1.Value
    martianterrain.links.new(math_019.outputs[0], group_008_1.inputs[0])
    # position_006.Position -> sample_index_001.Value
    martianterrain.links.new(position_006.outputs[0], sample_index_001.inputs[1])
    # math_017.Value -> math_018.Value
    martianterrain.links.new(math_017.outputs[0], math_018.inputs[1])
    # math_022.Value -> math_020.Value
    martianterrain.links.new(math_022.outputs[0], math_020.inputs[0])
    # reroute_023.Output -> math_020.Value
    martianterrain.links.new(reroute_023.outputs[0], math_020.inputs[1])
    # vector_math_001_1.Value -> math_018.Value
    martianterrain.links.new(vector_math_001_1.outputs[1], math_018.inputs[0])
    # reroute_021_1.Output -> math_017.Value
    martianterrain.links.new(reroute_021_1.outputs[0], math_017.inputs[0])
    # math_020.Value -> math_021.Value
    martianterrain.links.new(math_020.outputs[0], math_021.inputs[0])
    # math_016.Value -> distribute_points_on_faces_001.Distance Min
    martianterrain.links.new(
        math_016.outputs[0], distribute_points_on_faces_001.inputs[2]
    )
    # group_009_1.Value -> math_022.Value
    martianterrain.links.new(group_009_1.outputs[0], math_022.inputs[1])
    # reroute_020_1.Output -> sample_index_001.Geometry
    martianterrain.links.new(reroute_020_1.outputs[0], sample_index_001.inputs[0])
    # reroute_017_1.Output -> sample_nearest.Geometry
    martianterrain.links.new(reroute_017_1.outputs[0], sample_nearest.inputs[0])
    # sample_nearest.Index -> sample_index_001.Index
    martianterrain.links.new(sample_nearest.outputs[0], sample_index_001.inputs[2])
    # sample_nearest_001.Index -> sample_index_002.Index
    martianterrain.links.new(sample_nearest_001.outputs[0], sample_index_002.inputs[2])
    # compare_003.Result -> set_position_1.Selection
    martianterrain.links.new(compare_003.outputs[0], set_position_1.inputs[1])
    # group_008_1.Value -> math_022.Value
    martianterrain.links.new(group_008_1.outputs[0], math_022.inputs[0])
    # separate_xyz_004.X -> combine_xyz_003.X
    martianterrain.links.new(separate_xyz_004.outputs[0], combine_xyz_003.inputs[0])
    # separate_xyz_004.Y -> combine_xyz_003.Y
    martianterrain.links.new(separate_xyz_004.outputs[1], combine_xyz_003.inputs[1])
    # combine_xyz_003.Vector -> vector_math_001_1.Vector
    martianterrain.links.new(combine_xyz_003.outputs[0], vector_math_001_1.inputs[0])
    # separate_xyz_005.X -> combine_xyz_004.X
    martianterrain.links.new(separate_xyz_005.outputs[0], combine_xyz_004.inputs[0])
    # separate_xyz_005.Y -> combine_xyz_004.Y
    martianterrain.links.new(separate_xyz_005.outputs[1], combine_xyz_004.inputs[1])
    # sample_index_001.Value -> separate_xyz_005.Vector
    martianterrain.links.new(sample_index_001.outputs[0], separate_xyz_005.inputs[0])
    # combine_xyz_004.Vector -> vector_math_001_1.Vector
    martianterrain.links.new(combine_xyz_004.outputs[0], vector_math_001_1.inputs[1])
    # position_006.Position -> separate_xyz_004.Vector
    martianterrain.links.new(position_006.outputs[0], separate_xyz_004.inputs[0])
    # math_023.Value -> random_value_1.Seed
    martianterrain.links.new(math_023.outputs[0], random_value_1.inputs[8])
    # sample_nearest_001.Index -> sample_index_003.Index
    martianterrain.links.new(sample_nearest_001.outputs[0], sample_index_003.inputs[2])
    # math_021.Value -> vector_math_003_1.Vector
    martianterrain.links.new(math_021.outputs[0], vector_math_003_1.inputs[0])
    # mix_001.Result -> vector_math_003_1.Vector
    martianterrain.links.new(mix_001.outputs[1], vector_math_003_1.inputs[1])
    # reroute_017_1.Output -> reroute_020_1.Input
    martianterrain.links.new(reroute_017_1.outputs[0], reroute_020_1.inputs[0])
    # sample_index_002.Value -> reroute_021_1.Input
    martianterrain.links.new(sample_index_002.outputs[0], reroute_021_1.inputs[0])
    # sample_index_003.Value -> reroute_022_1.Input
    martianterrain.links.new(sample_index_003.outputs[0], reroute_022_1.inputs[0])
    # reroute_021_1.Output -> reroute_023.Input
    martianterrain.links.new(reroute_021_1.outputs[0], reroute_023.inputs[0])
    # distribute_points_on_faces_001.Points -> reroute_017_1.Input
    martianterrain.links.new(
        distribute_points_on_faces_001.outputs[0], reroute_017_1.inputs[0]
    )
    # distribute_points_on_faces_001.Points -> sample_nearest_001.Geometry
    martianterrain.links.new(
        distribute_points_on_faces_001.outputs[0], sample_nearest_001.inputs[0]
    )
    # store_named_attribute_001.Geometry -> sample_index_002.Geometry
    martianterrain.links.new(
        store_named_attribute_001.outputs[0], sample_index_002.inputs[0]
    )
    # store_named_attribute.Geometry -> sample_index_003.Geometry
    martianterrain.links.new(
        store_named_attribute.outputs[0], sample_index_003.inputs[0]
    )
    # distribute_points_on_faces_001.Points -> store_named_attribute_001.Geometry
    martianterrain.links.new(
        distribute_points_on_faces_001.outputs[0], store_named_attribute_001.inputs[0]
    )
    # distribute_points_on_faces_001.Points -> store_named_attribute.Geometry
    martianterrain.links.new(
        distribute_points_on_faces_001.outputs[0], store_named_attribute.inputs[0]
    )
    # string_001.String -> store_named_attribute_001.Name
    martianterrain.links.new(string_001.outputs[0], store_named_attribute_001.inputs[2])
    # string_001.String -> named_attribute.Name
    martianterrain.links.new(string_001.outputs[0], named_attribute.inputs[0])
    # named_attribute.Attribute -> sample_index_002.Value
    martianterrain.links.new(named_attribute.outputs[0], sample_index_002.inputs[1])
    # string.String -> store_named_attribute.Name
    martianterrain.links.new(string.outputs[0], store_named_attribute.inputs[2])
    # string.String -> named_attribute_001.Name
    martianterrain.links.new(string.outputs[0], named_attribute_001.inputs[0])
    # named_attribute_001.Attribute -> sample_index_003.Value
    martianterrain.links.new(named_attribute_001.outputs[0], sample_index_003.inputs[1])
    # distribute_points_on_faces_001.Normal -> store_named_attribute.Value
    martianterrain.links.new(
        distribute_points_on_faces_001.outputs[1], store_named_attribute.inputs[3]
    )
    # random_value_1.Value -> float_curve_002.Value
    martianterrain.links.new(random_value_1.outputs[1], float_curve_002.inputs[1])
    # float_curve_002.Value -> store_named_attribute_001.Value
    martianterrain.links.new(
        float_curve_002.outputs[0], store_named_attribute_001.inputs[3]
    )
    # reroute_025.Output -> group_008_1.Crater Radius Fraction
    martianterrain.links.new(reroute_025.outputs[0], group_008_1.inputs[1])
    # reroute_025.Output -> group_009_1.Crater Radius Fraction
    martianterrain.links.new(reroute_025.outputs[0], group_009_1.inputs[1])
    # reroute_021_1.Output -> reroute_025.Input
    martianterrain.links.new(reroute_021_1.outputs[0], reroute_025.inputs[0])
    # reroute_022_1.Output -> mix_001.B
    martianterrain.links.new(reroute_022_1.outputs[0], mix_001.inputs[5])
    # reroute_026.Output -> group_009_1.Seed
    martianterrain.links.new(reroute_026.outputs[0], group_009_1.inputs[3])
    # reroute_026.Output -> group_008_1.Seed
    martianterrain.links.new(reroute_026.outputs[0], group_008_1.inputs[3])
    # position_007.Position -> vector_math_004_1.Vector
    martianterrain.links.new(position_007.outputs[0], vector_math_004_1.inputs[0])
    # vector_math_003_1.Vector -> vector_math_004_1.Vector
    martianterrain.links.new(vector_math_003_1.outputs[0], vector_math_004_1.inputs[1])
    # vector_math_004_1.Vector -> set_position_1.Position
    martianterrain.links.new(vector_math_004_1.outputs[0], set_position_1.inputs[2])
    # reroute_027.Output -> group_008_1.Max Crater Radius
    martianterrain.links.new(reroute_027.outputs[0], group_008_1.inputs[2])
    # reroute_027.Output -> group_009_1.Max Crater Radius
    martianterrain.links.new(reroute_027.outputs[0], group_009_1.inputs[2])
    # math_024.Value -> mix_001.Factor
    martianterrain.links.new(math_024.outputs[0], mix_001.inputs[0])
    # math_025.Value -> math_024.Value
    martianterrain.links.new(math_025.outputs[0], math_024.inputs[1])
    # reroute_023.Output -> math_025.Value
    martianterrain.links.new(reroute_023.outputs[0], math_025.inputs[1])
    # math_006_1.Value -> math_016.Value
    martianterrain.links.new(math_006_1.outputs[0], math_016.inputs[0])
    # math_007_1.Value -> math_021.Value
    martianterrain.links.new(math_007_1.outputs[0], math_021.inputs[1])
    # reroute_028.Output -> distribute_points_on_faces_001.Mesh
    martianterrain.links.new(
        reroute_028.outputs[0], distribute_points_on_faces_001.inputs[0]
    )
    # reroute_024.Output -> math_017.Value
    martianterrain.links.new(reroute_024.outputs[0], math_017.inputs[1])
    # reroute_028.Output -> set_position_1.Geometry
    martianterrain.links.new(reroute_028.outputs[0], set_position_1.inputs[0])
    # reroute_024.Output -> reroute_027.Input
    martianterrain.links.new(reroute_024.outputs[0], reroute_027.inputs[0])
    # group_005_1.Value -> math_024.Value
    martianterrain.links.new(group_005_1.outputs[0], math_024.inputs[0])
    # reroute_033.Output -> distribute_points_on_faces.Mesh
    martianterrain.links.new(
        reroute_033.outputs[0], distribute_points_on_faces.inputs[0]
    )
    # transform_geometry_001_1.Geometry -> reroute_028.Input
    martianterrain.links.new(transform_geometry_001_1.outputs[0], reroute_028.inputs[0])
    # reroute_030.Output -> reroute_016.Input
    martianterrain.links.new(reroute_030.outputs[0], reroute_016.inputs[0])
    # reroute_016.Output -> reroute_031.Input
    martianterrain.links.new(reroute_016.outputs[0], reroute_031.inputs[0])
    # set_position_1.Geometry -> reroute_033.Input
    martianterrain.links.new(set_position_1.outputs[0], reroute_033.inputs[0])
    # reroute_008.Output -> reroute_032.Input
    martianterrain.links.new(reroute_008.outputs[0], reroute_032.inputs[0])
    # group_002_1.Value -> distribute_points_on_faces_001.Density Factor
    martianterrain.links.new(
        group_002_1.outputs[0], distribute_points_on_faces_001.inputs[5]
    )
    # reroute_002_2.Output -> reroute_029.Input
    martianterrain.links.new(reroute_002_2.outputs[0], reroute_029.inputs[0])
    # reroute_029.Output -> distribute_points_on_faces_001.Seed
    martianterrain.links.new(
        reroute_029.outputs[0], distribute_points_on_faces_001.inputs[6]
    )
    # reroute_029.Output -> math_023.Value
    martianterrain.links.new(reroute_029.outputs[0], math_023.inputs[0])
    # reroute_030.Output -> reroute_026.Input
    martianterrain.links.new(reroute_030.outputs[0], reroute_026.inputs[0])
    # reroute_029.Output -> reroute_030.Input
    martianterrain.links.new(reroute_029.outputs[0], reroute_030.inputs[0])
    # math_006_1.Value -> reroute_024.Input
    martianterrain.links.new(math_006_1.outputs[0], reroute_024.inputs[0])
    # reroute_024.Output -> reroute_035.Input
    martianterrain.links.new(reroute_024.outputs[0], reroute_035.inputs[0])
    # separate_xyz_002_1.X -> combine_xyz_005.X
    martianterrain.links.new(separate_xyz_002_1.outputs[0], combine_xyz_005.inputs[0])
    # separate_xyz_002_1.Y -> combine_xyz_005.Y
    martianterrain.links.new(separate_xyz_002_1.outputs[1], combine_xyz_005.inputs[1])
    # combine_xyz_005.Vector -> vector_math_005.Vector
    martianterrain.links.new(combine_xyz_005.outputs[0], vector_math_005.inputs[0])
    # vector_math_005.Value -> compare_004.A
    martianterrain.links.new(vector_math_005.outputs[1], compare_004.inputs[0])
    # compare_004.Result -> boolean_math_001.Boolean
    martianterrain.links.new(compare_004.outputs[0], boolean_math_001.inputs[0])
    # boolean_math_1.Boolean -> boolean_math_001.Boolean
    martianterrain.links.new(boolean_math_1.outputs[0], boolean_math_001.inputs[1])
    # boolean_math_001.Boolean -> delete_geometry_1.Selection
    martianterrain.links.new(boolean_math_001.outputs[0], delete_geometry_1.inputs[1])
    # reroute_004_1.Output -> reroute_034.Input
    martianterrain.links.new(reroute_004_1.outputs[0], reroute_034.inputs[0])
    # reroute_034.Output -> compare_004.B
    martianterrain.links.new(reroute_034.outputs[0], compare_004.inputs[1])
    # separate_xyz_003_1.X -> mix_002.A
    martianterrain.links.new(separate_xyz_003_1.outputs[0], mix_002.inputs[2])
    # separate_xyz_003_1.Y -> mix_002.B
    martianterrain.links.new(separate_xyz_003_1.outputs[1], mix_002.inputs[3])
    # group_010_1.Value -> math_026.Value
    martianterrain.links.new(group_010_1.outputs[0], math_026.inputs[1])
    # mix_002.Result -> math_026.Value
    martianterrain.links.new(mix_002.outputs[0], math_026.inputs[0])
    # math_026.Value -> math_027.Value
    martianterrain.links.new(math_026.outputs[0], math_027.inputs[0])
    # math_027.Value -> math_028.Value
    martianterrain.links.new(math_027.outputs[0], math_028.inputs[0])
    # math_028.Value -> distribute_points_on_faces.Distance Min
    martianterrain.links.new(math_028.outputs[0], distribute_points_on_faces.inputs[2])
    # group_011_1.Value -> distribute_points_on_faces.Density Factor
    martianterrain.links.new(
        group_011_1.outputs[0], distribute_points_on_faces.inputs[5]
    )
    # reroute_031.Output -> reroute_036.Input
    martianterrain.links.new(reroute_031.outputs[0], reroute_036.inputs[0])
    # reroute_036.Output -> group_011_1.Seed
    martianterrain.links.new(reroute_036.outputs[0], group_011_1.inputs[3])
    # float_curve_001.Value -> math_029.Value
    martianterrain.links.new(float_curve_001.outputs[0], math_029.inputs[0])
    # math_027.Value -> math_029.Value
    martianterrain.links.new(math_027.outputs[0], math_029.inputs[1])
    # position_008.Position -> attribute_statistic_1.Attribute
    martianterrain.links.new(position_008.outputs[0], attribute_statistic_1.inputs[2])
    # attribute_statistic_1.Range -> separate_xyz_006.Vector
    martianterrain.links.new(
        attribute_statistic_1.outputs[5], separate_xyz_006.inputs[0]
    )
    # separate_xyz_006.Z -> combine_xyz_006.Z
    martianterrain.links.new(separate_xyz_006.outputs[2], combine_xyz_006.inputs[2])
    # vector_math_1.Vector -> transform_geometry_003_1.Translation
    martianterrain.links.new(
        vector_math_1.outputs[0], transform_geometry_003_1.inputs[1]
    )
    # sample_index.Value -> vector_math_1.Vector
    martianterrain.links.new(sample_index.outputs[0], vector_math_1.inputs[0])
    # math_029.Value -> transform_geometry_004.Scale
    martianterrain.links.new(math_029.outputs[0], transform_geometry_004.inputs[3])
    # transform_geometry_004.Geometry -> transform_geometry_003_1.Geometry
    martianterrain.links.new(
        transform_geometry_004.outputs[0], transform_geometry_003_1.inputs[0]
    )
    # group_001_1.Geometry -> transform_geometry_004.Geometry
    martianterrain.links.new(group_001_1.outputs[0], transform_geometry_004.inputs[0])
    # transform_geometry_004.Geometry -> attribute_statistic_1.Geometry
    martianterrain.links.new(
        transform_geometry_004.outputs[0], attribute_statistic_1.inputs[0]
    )
    # vector_math_006.Vector -> vector_math_1.Vector
    martianterrain.links.new(vector_math_006.outputs[0], vector_math_1.inputs[1])
    # combine_xyz_006.Vector -> vector_math_006.Vector
    martianterrain.links.new(combine_xyz_006.outputs[0], vector_math_006.inputs[0])
    # reroute_019_1.Output -> group_012_1.Seed
    martianterrain.links.new(reroute_019_1.outputs[0], group_012_1.inputs[2])
    # group_012_1.Value -> vector_math_006.Scale
    martianterrain.links.new(group_012_1.outputs[0], vector_math_006.inputs[3])
    # group_input_4.Density -> reroute_040.Input
    martianterrain.links.new(group_input_4.outputs[2], reroute_040.inputs[0])
    # reroute_038.Output -> math_015.Value
    martianterrain.links.new(reroute_038.outputs[0], math_015.inputs[1])
    # reroute_040.Output -> reroute_038.Input
    martianterrain.links.new(reroute_040.outputs[0], reroute_038.inputs[0])
    # math_029.Value -> math_015.Value
    martianterrain.links.new(math_029.outputs[0], math_015.inputs[0])
    # math_015.Value -> math_030.Value
    martianterrain.links.new(math_015.outputs[0], math_030.inputs[0])
    # math_030.Value -> float_to_integer_001.Float
    martianterrain.links.new(math_030.outputs[0], float_to_integer_001.inputs[0])
    # float_to_integer_001.Integer -> group_001_1.Subdivisions
    martianterrain.links.new(float_to_integer_001.outputs[0], group_001_1.inputs[1])
    # join_geometry.Geometry -> switch_2.False
    martianterrain.links.new(join_geometry.outputs[0], switch_2.inputs[1])
    # reroute_033.Output -> reroute_037.Input
    martianterrain.links.new(reroute_033.outputs[0], reroute_037.inputs[0])
    # repeat_output.Geometry -> mesh_boolean_1.Mesh 2
    martianterrain.links.new(repeat_output.outputs[0], mesh_boolean_1.inputs[1])
    # mesh_boolean_1.Mesh -> switch_2.True
    martianterrain.links.new(mesh_boolean_1.outputs[0], switch_2.inputs[2])
    # reroute_041.Output -> switch_2.Switch
    martianterrain.links.new(reroute_041.outputs[0], switch_2.inputs[0])
    # group_input_4.Rock Mesh Boolean -> reroute_039.Input
    martianterrain.links.new(group_input_4.outputs[4], reroute_039.inputs[0])
    # reroute_039.Output -> reroute_041.Input
    martianterrain.links.new(reroute_039.outputs[0], reroute_041.inputs[0])
    # value.Value -> math_027.Value
    martianterrain.links.new(value.outputs[0], math_027.inputs[1])
    # transform_geometry_003_1.Geometry -> join_geometry_001.Geometry
    martianterrain.links.new(
        transform_geometry_003_1.outputs[0], join_geometry_001.inputs[0]
    )
    # reroute_037.Output -> join_geometry.Geometry
    martianterrain.links.new(reroute_037.outputs[0], join_geometry.inputs[0])
    # reroute_037.Output -> mesh_boolean_1.Mesh 2
    martianterrain.links.new(reroute_037.outputs[0], mesh_boolean_1.inputs[1])
    return martianterrain


martianterrain = martianterrain_node_group()
