<?php
function getRawContentUrl($url){
  $pieces = explode('/', $url);

  // replacing 6th index (blob) with raw to get xml content
  if(sizeof($pieces) > 6)
    $pieces[5] = 'raw';
  else
    return $url;
  return join('/', $pieces);
}


function traverseNode($root,$parent){
  if(!is_array($parent->children)){
    $parent->children = [];
  }
  foreach ($root->childNodes as $node) {
    $rootNode = new stdClass;
    $rootNode->name = $node->nodeName;
    $rootNode->content = $node->textContent;
    array_push($parent->children, $rootNode);
    if($node->hasChildNodes()){
      traverseNode($node,$parent);
    }
  }
}
$link = "https://github.com/SwiftOnSecurity/sysmon-config/blob/master/sysmonconfig-export.xml";

$rawUrl = getRawContentUrl($link);

$xmlContent = file_get_contents($rawUrl);

$xmlDoc = new DOMDocument();
$xmlDoc->loadXML($xmlContent);
$xmlDoc->saveXML();
$parent = new stdClass;
$parent->name = 'root';
$parent->children = [];
traverseNode($xmlDoc,$parent);

var_dump($parent);









 ?>
