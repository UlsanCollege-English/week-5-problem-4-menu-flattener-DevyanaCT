def flatten_menu(node):
    """
    Return a flat list of item names from a nested menu.
    Node has "type": "category" or "item".
    """
    if node is None or not isinstance(node, dict):
        return []

    node_type = node.get("type")

    if node_type == "item":
        name = node.get("name")
        # Only include if name exists
        return [name] if name is not None else []

    if node_type == "category":
        items = []
        for child in node.get("children", []):
            items.extend(flatten_menu(child))
        return items

    # Unknown type → ignore
    return []
