"""
Keep custom types in a single file
"""
from typing import List, Dict, Any

YamlDataType = Dict[str, Any]
YamlDatalistType = List[YamlDataType]
RuleDataType = YamlDatalistType
ConfigDataType = Dict[str, Dict[Any, Any]]
