<?php
namespace TypeNetwork\VideoProof;
require_once(__DIR__ . "/videoproof.inc");

$videoproof = new VideoProof();

print $videoproof->pageHead('Video Proof');
print $videoproof->pageSections();
print $videoproof->pageFoot();
