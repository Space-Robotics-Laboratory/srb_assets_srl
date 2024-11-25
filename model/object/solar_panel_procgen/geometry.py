import bpy
import mathutils


# initialize solarpanel node group
def solarpanel_node_group():
    solarpanel = bpy.data.node_groups.new(type="GeometryNodeTree", name="SolarPanel")

    solarpanel.color_tag = "GEOMETRY"
    solarpanel.description = ""
    solarpanel.default_group_node_width = 140

    solarpanel.is_modifier = True

    # solarpanel interface
    # Socket Geometry
    geometry_socket = solarpanel.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket.attribute_domain = "POINT"

    # Socket seed
    seed_socket = solarpanel.interface.new_socket(
        name="seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket.default_value = 0
    seed_socket.min_value = 0
    seed_socket.max_value = 2147483647
    seed_socket.subtype = "NONE"
    seed_socket.attribute_domain = "POINT"
    seed_socket.hide_value = True
    seed_socket.hide_in_modifier = True
    seed_socket.force_non_field = True

    # Socket scale
    scale_socket = solarpanel.interface.new_socket(
        name="scale", in_out="INPUT", socket_type="NodeSocketVector"
    )
    scale_socket.default_value = (1.0, 1.0, 0.05000000074505806)
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e38
    scale_socket.subtype = "TRANSLATION"
    scale_socket.attribute_domain = "POINT"
    scale_socket.force_non_field = True

    # Socket border_size
    border_size_socket = solarpanel.interface.new_socket(
        name="border_size", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    border_size_socket.default_value = 0.009999999776482582
    border_size_socket.min_value = 0.0
    border_size_socket.max_value = 3.4028234663852886e38
    border_size_socket.subtype = "DISTANCE"
    border_size_socket.attribute_domain = "POINT"
    border_size_socket.force_non_field = True

    # Socket panel_depth
    panel_depth_socket = solarpanel.interface.new_socket(
        name="panel_depth", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    panel_depth_socket.default_value = 0.0020000000949949026
    panel_depth_socket.min_value = 0.0
    panel_depth_socket.max_value = 3.4028234663852886e38
    panel_depth_socket.subtype = "DISTANCE"
    panel_depth_socket.attribute_domain = "POINT"
    panel_depth_socket.force_non_field = True

    # Socket with_back_panel
    with_back_panel_socket = solarpanel.interface.new_socket(
        name="with_back_panel", in_out="INPUT", socket_type="NodeSocketBool"
    )
    with_back_panel_socket.default_value = False
    with_back_panel_socket.attribute_domain = "POINT"

    # Socket frame_mat
    frame_mat_socket = solarpanel.interface.new_socket(
        name="frame_mat", in_out="INPUT", socket_type="NodeSocketMaterial"
    )
    frame_mat_socket.attribute_domain = "POINT"

    # Socket cells_mat
    cells_mat_socket = solarpanel.interface.new_socket(
        name="cells_mat", in_out="INPUT", socket_type="NodeSocketMaterial"
    )
    cells_mat_socket.attribute_domain = "POINT"

    # initialize solarpanel nodes
    # node Group Input
    group_input = solarpanel.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # node Group Output
    group_output = solarpanel.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # node Set Material
    set_material = solarpanel.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"

    # node Integer.001
    integer_001 = solarpanel.nodes.new("FunctionNodeInputInt")
    integer_001.label = "Global Seed Offset"
    integer_001.name = "Integer.001"
    integer_001.mute = True
    integer_001.integer = 0

    # node Grid
    grid = solarpanel.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    # Vertices X
    grid.inputs[2].default_value = 2
    # Vertices Y
    grid.inputs[3].default_value = 2

    # node Extrude Mesh
    extrude_mesh = solarpanel.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = "FACES"
    # Selection
    extrude_mesh.inputs[1].default_value = True
    # Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh.inputs[4].default_value = False

    # node Extrude Mesh.001
    extrude_mesh_001 = solarpanel.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_001.name = "Extrude Mesh.001"
    extrude_mesh_001.mode = "FACES"
    # Offset
    extrude_mesh_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh_001.inputs[4].default_value = False

    # node Extrude Mesh.002
    extrude_mesh_002 = solarpanel.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_002.name = "Extrude Mesh.002"
    extrude_mesh_002.mode = "FACES"
    # Individual
    extrude_mesh_002.inputs[4].default_value = False

    # node Vector
    vector = solarpanel.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (0.0, 0.0, -1.0)

    # node Set Material.002
    set_material_002 = solarpanel.nodes.new("GeometryNodeSetMaterial")
    set_material_002.name = "Set Material.002"
    # Selection
    set_material_002.inputs[1].default_value = True

    # node Capture Attribute
    capture_attribute = solarpanel.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new("FLOAT", "Index")
    capture_attribute.capture_items["Index"].data_type = "INT"
    capture_attribute.domain = "POINT"

    # node Index
    index = solarpanel.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    # node Delete Geometry
    delete_geometry = solarpanel.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = "POINT"
    delete_geometry.mode = "ALL"

    # node Compare
    compare = solarpanel.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = "INT"
    compare.mode = "ELEMENT"
    compare.operation = "EQUAL"

    # node Mesh to Curve
    mesh_to_curve = solarpanel.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"

    # node Position
    position = solarpanel.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    # node Separate XYZ
    separate_xyz = solarpanel.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[0].hide = True
    separate_xyz.outputs[1].hide = True

    # node Compare.001
    compare_001 = solarpanel.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = "FLOAT"
    compare_001.mode = "ELEMENT"
    compare_001.operation = "EQUAL"
    # B
    compare_001.inputs[1].default_value = 0.0
    # Epsilon
    compare_001.inputs[12].default_value = 0.0

    # node Fill Curve
    fill_curve = solarpanel.nodes.new("GeometryNodeFillCurve")
    fill_curve.name = "Fill Curve"
    fill_curve.mode = "NGONS"
    # Group ID
    fill_curve.inputs[1].default_value = 0

    # node Join Geometry
    join_geometry = solarpanel.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # node Merge by Distance
    merge_by_distance = solarpanel.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = "ALL"
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Distance
    merge_by_distance.inputs[2].default_value = 9.999999747378752e-05

    # node Frame
    frame = solarpanel.nodes.new("NodeFrame")
    frame.label = "fill bottom face"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # node Frame.001
    frame_001 = solarpanel.nodes.new("NodeFrame")
    frame_001.label = "base geometry"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # node Frame.002
    frame_002 = solarpanel.nodes.new("NodeFrame")
    frame_002.label = "recede panel"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # node Reroute
    reroute = solarpanel.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketBool"
    # node Reroute.001
    reroute_001 = solarpanel.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketBool"
    # node Reroute.002
    reroute_002 = solarpanel.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketInt"
    # node Reroute.003
    reroute_003 = solarpanel.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketGeometry"
    # node Reroute.004
    reroute_004 = solarpanel.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketGeometry"
    # node Reroute.005
    reroute_005 = solarpanel.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketGeometry"
    # node Switch
    switch = solarpanel.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = "GEOMETRY"

    # node Integer Math
    integer_math = solarpanel.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.mute = True
    integer_math.operation = "ADD"

    # node Reroute.006
    reroute_006 = solarpanel.nodes.new("NodeReroute")
    reroute_006.label = "seed"
    reroute_006.name = "Reroute.006"
    reroute_006.mute = True
    reroute_006.socket_idname = "NodeSocketInt"
    # node Separate XYZ.001
    separate_xyz_001 = solarpanel.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"

    # node Reroute.007
    reroute_007 = solarpanel.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketFloatDistance"
    # node Reroute.008
    reroute_008 = solarpanel.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketFloatDistance"
    # node Reroute.009
    reroute_009 = solarpanel.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.socket_idname = "NodeSocketBool"
    # node Merge by Distance.001
    merge_by_distance_001 = solarpanel.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.mode = "ALL"
    # Selection
    merge_by_distance_001.inputs[1].default_value = True
    # Distance
    merge_by_distance_001.inputs[2].default_value = 9.999999747378752e-05

    # node Switch.001
    switch_001 = solarpanel.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = "GEOMETRY"

    # node Compare.002
    compare_002 = solarpanel.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = "FLOAT"
    compare_002.mode = "ELEMENT"
    compare_002.operation = "EQUAL"
    # B
    compare_002.inputs[1].default_value = 0.0
    # Epsilon
    compare_002.inputs[12].default_value = 0.0

    # node Reroute.010
    reroute_010 = solarpanel.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.socket_idname = "NodeSocketGeometry"

    # Set parents
    grid.parent = frame_001
    extrude_mesh.parent = frame_001
    extrude_mesh_001.parent = frame_001
    extrude_mesh_002.parent = frame_002
    vector.parent = frame_002
    capture_attribute.parent = frame_001
    index.parent = frame_001
    delete_geometry.parent = frame_001
    compare.parent = frame_001
    mesh_to_curve.parent = frame
    position.parent = frame
    separate_xyz.parent = frame
    compare_001.parent = frame
    fill_curve.parent = frame
    join_geometry.parent = frame
    merge_by_distance.parent = frame
    reroute.parent = frame_002
    reroute_001.parent = frame_001
    reroute_002.parent = frame_001
    reroute_003.parent = frame
    reroute_004.parent = frame
    reroute_005.parent = frame
    switch.parent = frame
    reroute_007.parent = frame_001
    reroute_008.parent = frame_002
    merge_by_distance_001.parent = frame_002
    switch_001.parent = frame_002
    compare_002.parent = frame_002
    reroute_010.parent = frame_002

    # Set locations
    group_input.location = (-2245.719482421875, 154.1492462158203)
    group_output.location = (2629.999755859375, 0.0)
    set_material.location = (2439.999755859375, 23.5)
    integer_001.location = (-2245.719482421875, 248.1492462158203)
    grid.location = (-600.000244140625, 45.5)
    extrude_mesh.location = (-220.000244140625, 79.49999237060547)
    extrude_mesh_001.location = (-30.000244140625, 79.49999237060547)
    extrude_mesh_002.location = (2059.999755859375, 79.49998474121094)
    vector.location = (1869.999755859375, -84.71499633789062)
    set_material_002.location = (2249.999755859375, 53.30263900756836)
    capture_attribute.location = (-410.000244140625, 23.5)
    index.location = (-600.000244140625, -154.14312744140625)
    delete_geometry.location = (349.999755859375, 86.33111572265625)
    compare.location = (159.999755859375, -55.73487854003906)
    mesh_to_curve.location = (1299.999755859375, 379.2769470214844)
    position.location = (729.999755859375, 355.7769470214844)
    separate_xyz.location = (919.999755859375, 355.40728759765625)
    compare_001.location = (1109.999755859375, 414.7769470214844)
    fill_curve.location = (1489.999755859375, 391.2769470214844)
    join_geometry.location = (1679.999755859375, 368.2769470214844)
    merge_by_distance.location = (1869.999755859375, 402.2769470214844)
    frame.location = (-1040.5667724609375, -150.7635498046875)
    frame_001.location = (-889.3734130859375, 304.94390869140625)
    frame_002.location = (-632.2884521484375, 312.48724365234375)
    reroute.location = (1890.416748046875, 127.94869995117188)
    reroute_001.location = (-29.37310791015625, 135.49200439453125)
    reroute_002.location = (-239.9327392578125, -165.74472045898438)
    reroute_003.location = (736.4287719726562, 434.59149169921875)
    reroute_004.location = (1261.0093994140625, 434.59149169921875)
    reroute_005.location = (1636.045654296875, 434.59149169921875)
    switch.location = (2059.999755859375, 543.2854614257812)
    integer_math.location = (-2055.719482421875, 270.14923095703125)
    reroute_006.location = (-1895.7193603515625, 235.1492462158203)
    separate_xyz_001.location = (-1694.7052001953125, 244.05198669433594)
    reroute_007.location = (-83.75711059570312, -219.44503784179688)
    reroute_008.location = (2013.187255859375, -235.79827880859375)
    reroute_009.location = (954.8936767578125, 46.95509338378906)
    merge_by_distance_001.location = (2410.55712890625, -138.453125)
    switch_001.location = (2610.46142578125, 92.11172485351562)
    compare_002.location = (2220.55712890625, -77.42880249023438)
    reroute_010.location = (2350.07421875, 15.891845703125)

    # initialize solarpanel links
    # set_material.Geometry -> group_output.Geometry
    solarpanel.links.new(set_material.outputs[0], group_output.inputs[0])
    # capture_attribute.Geometry -> extrude_mesh.Mesh
    solarpanel.links.new(capture_attribute.outputs[0], extrude_mesh.inputs[0])
    # extrude_mesh.Side -> extrude_mesh_001.Selection
    solarpanel.links.new(extrude_mesh.outputs[2], extrude_mesh_001.inputs[1])
    # reroute.Output -> extrude_mesh_002.Selection
    solarpanel.links.new(reroute.outputs[0], extrude_mesh_002.inputs[1])
    # vector.Vector -> extrude_mesh_002.Offset
    solarpanel.links.new(vector.outputs[0], extrude_mesh_002.inputs[2])
    # set_material_002.Geometry -> set_material.Geometry
    solarpanel.links.new(set_material_002.outputs[0], set_material.inputs[0])
    # extrude_mesh_002.Top -> set_material.Selection
    solarpanel.links.new(extrude_mesh_002.outputs[1], set_material.inputs[1])
    # grid.Mesh -> capture_attribute.Geometry
    solarpanel.links.new(grid.outputs[0], capture_attribute.inputs[0])
    # index.Index -> capture_attribute.Index
    solarpanel.links.new(index.outputs[0], capture_attribute.inputs[1])
    # reroute_002.Output -> compare.A
    solarpanel.links.new(reroute_002.outputs[0], compare.inputs[2])
    # index.Index -> compare.B
    solarpanel.links.new(index.outputs[0], compare.inputs[3])
    # compare.Result -> delete_geometry.Selection
    solarpanel.links.new(compare.outputs[0], delete_geometry.inputs[1])
    # extrude_mesh.Mesh -> extrude_mesh_001.Mesh
    solarpanel.links.new(extrude_mesh.outputs[0], extrude_mesh_001.inputs[0])
    # extrude_mesh_001.Mesh -> delete_geometry.Geometry
    solarpanel.links.new(extrude_mesh_001.outputs[0], delete_geometry.inputs[0])
    # position.Position -> separate_xyz.Vector
    solarpanel.links.new(position.outputs[0], separate_xyz.inputs[0])
    # separate_xyz.Z -> compare_001.A
    solarpanel.links.new(separate_xyz.outputs[2], compare_001.inputs[0])
    # compare_001.Result -> mesh_to_curve.Selection
    solarpanel.links.new(compare_001.outputs[0], mesh_to_curve.inputs[1])
    # mesh_to_curve.Curve -> fill_curve.Curve
    solarpanel.links.new(mesh_to_curve.outputs[0], fill_curve.inputs[0])
    # join_geometry.Geometry -> merge_by_distance.Geometry
    solarpanel.links.new(join_geometry.outputs[0], merge_by_distance.inputs[0])
    # reroute_004.Output -> mesh_to_curve.Mesh
    solarpanel.links.new(reroute_004.outputs[0], mesh_to_curve.inputs[0])
    # reroute_001.Output -> reroute.Input
    solarpanel.links.new(reroute_001.outputs[0], reroute.inputs[0])
    # extrude_mesh.Top -> reroute_001.Input
    solarpanel.links.new(extrude_mesh.outputs[1], reroute_001.inputs[0])
    # capture_attribute.Index -> reroute_002.Input
    solarpanel.links.new(capture_attribute.outputs[1], reroute_002.inputs[0])
    # reroute_003.Output -> reroute_004.Input
    solarpanel.links.new(reroute_003.outputs[0], reroute_004.inputs[0])
    # reroute_004.Output -> reroute_005.Input
    solarpanel.links.new(reroute_004.outputs[0], reroute_005.inputs[0])
    # merge_by_distance.Geometry -> switch.True
    solarpanel.links.new(merge_by_distance.outputs[0], switch.inputs[2])
    # switch.Output -> extrude_mesh_002.Mesh
    solarpanel.links.new(switch.outputs[0], extrude_mesh_002.inputs[0])
    # reroute_005.Output -> switch.False
    solarpanel.links.new(reroute_005.outputs[0], switch.inputs[1])
    # fill_curve.Mesh -> join_geometry.Geometry
    solarpanel.links.new(fill_curve.outputs[0], join_geometry.inputs[0])
    # integer_001.Integer -> integer_math.Value
    solarpanel.links.new(integer_001.outputs[0], integer_math.inputs[0])
    # group_input.seed -> integer_math.Value
    solarpanel.links.new(group_input.outputs[0], integer_math.inputs[1])
    # integer_math.Value -> reroute_006.Input
    solarpanel.links.new(integer_math.outputs[0], reroute_006.inputs[0])
    # group_input.scale -> separate_xyz_001.Vector
    solarpanel.links.new(group_input.outputs[1], separate_xyz_001.inputs[0])
    # separate_xyz_001.X -> grid.Size X
    solarpanel.links.new(separate_xyz_001.outputs[0], grid.inputs[0])
    # separate_xyz_001.Y -> grid.Size Y
    solarpanel.links.new(separate_xyz_001.outputs[1], grid.inputs[1])
    # separate_xyz_001.Z -> extrude_mesh.Offset Scale
    solarpanel.links.new(separate_xyz_001.outputs[2], extrude_mesh.inputs[3])
    # reroute_007.Output -> extrude_mesh_001.Offset Scale
    solarpanel.links.new(reroute_007.outputs[0], extrude_mesh_001.inputs[3])
    # group_input.border_size -> reroute_007.Input
    solarpanel.links.new(group_input.outputs[2], reroute_007.inputs[0])
    # group_input.panel_depth -> reroute_008.Input
    solarpanel.links.new(group_input.outputs[3], reroute_008.inputs[0])
    # reroute_008.Output -> extrude_mesh_002.Offset Scale
    solarpanel.links.new(reroute_008.outputs[0], extrude_mesh_002.inputs[3])
    # group_input.with_back_panel -> reroute_009.Input
    solarpanel.links.new(group_input.outputs[4], reroute_009.inputs[0])
    # reroute_008.Output -> compare_002.A
    solarpanel.links.new(reroute_008.outputs[0], compare_002.inputs[0])
    # merge_by_distance_001.Geometry -> switch_001.True
    solarpanel.links.new(merge_by_distance_001.outputs[0], switch_001.inputs[2])
    # reroute_010.Output -> merge_by_distance_001.Geometry
    solarpanel.links.new(reroute_010.outputs[0], merge_by_distance_001.inputs[0])
    # reroute_010.Output -> switch_001.False
    solarpanel.links.new(reroute_010.outputs[0], switch_001.inputs[1])
    # switch_001.Output -> set_material_002.Geometry
    solarpanel.links.new(switch_001.outputs[0], set_material_002.inputs[0])
    # reroute_009.Output -> switch.Switch
    solarpanel.links.new(reroute_009.outputs[0], switch.inputs[0])
    # compare_002.Result -> switch_001.Switch
    solarpanel.links.new(compare_002.outputs[0], switch_001.inputs[0])
    # extrude_mesh_002.Mesh -> reroute_010.Input
    solarpanel.links.new(extrude_mesh_002.outputs[0], reroute_010.inputs[0])
    # group_input.frame_mat -> set_material_002.Material
    solarpanel.links.new(group_input.outputs[5], set_material_002.inputs[2])
    # group_input.cells_mat -> set_material.Material
    solarpanel.links.new(group_input.outputs[6], set_material.inputs[2])
    # delete_geometry.Geometry -> reroute_003.Input
    solarpanel.links.new(delete_geometry.outputs[0], reroute_003.inputs[0])
    # reroute_005.Output -> join_geometry.Geometry
    solarpanel.links.new(reroute_005.outputs[0], join_geometry.inputs[0])
    return solarpanel


solarpanel = solarpanel_node_group()
