def get_story_depth(node):
    """Get max depth from given node."""
    if not node.child_nodes.all():
        return 1
    
    return 1 + max([get_story_depth(node) for node in node.child_nodes.all()])
