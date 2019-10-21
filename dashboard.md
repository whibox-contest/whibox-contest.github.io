---
layout: base
title: Dashboard
edition: "2019"
---

{% include index_boxes.html %}

<hr>

<div class="row">
  <div class="col-xs-12">
    <h2>Challenges</h2>
  </div>
</div>

<div class="row">
  <div class="col-xs-12">
    <h3 id="challenges">Strawberry Ranking and Challenges</h3>
  	{% include table_challenges.html %}
  </div>
</div>

<div class="row">
  <div class="col-xs-12">
	<h3>Strawberry scores over time</h3>
    <div id="strawberryholder" style="height: 500px;"></div>
  </div>

  <div class="col-xs-12">
	<h3>Carrots scores over time</h3>
	<div id="carrotholder" style="height: 500px;"></div>
  </div>
</div>

<hr />

<div class="row">
  <div class="col-xs-12">
	<h2>Banana Scores</h2>
  </div>
</div>

<div class="row">
  <div class="col-xs-12 col-sm-10 col-md-8 col-lg-6">
	<h3 id="bananas">Banana Ranking</h3>
	{% include table_bananas_ranking.html %}
  </div>
</div><!-- row -->

<div class="row">
  <div class="col-xs-12 col-sm-10 col-md-8 col-lg-6">
	<h3 id="breaks">All Challenge Breaks</h3>
	{% include table_breaks.html %}
  </div>

  <div class="col-xs-12 col-sm-10 col-md-8 col-lg-6">
	<h3 id="breaks">All Challenge Inversions </h3>
	{% include table_inverts.html %}
  </div>
</div><!-- row -->

<script type="text/javascript">
      function getProgramsToPlot() {
	  var programs = [ {id:111,name:"goofy_lichterman",ts_publish:1564601833,ts_break:-1,ts_invert:-1,performance:7.7342693436,color:"hsl(259, 100%, 53%)"}, {id:115,name:"elegant_turing",ts_publish:1564608634,ts_break:-1,ts_invert:-1,performance:6.5029780767,color:"hsl(185, 100%, 39%)"}, {id:100,name:"hopeful_kirch",ts_publish:1564344825,ts_break:-1,ts_invert:-1,performance:3.0697066710,color:"hsl(37, 100%, 41%)"}, {id:90,name:"wonderful_feynman",ts_publish:1563749572,ts_break:1564926361,ts_invert:1564926337,performance:3.9255600339,color:"hsl(9, 100%, 43%)"}, {id:35,name:"friendly_edison",ts_publish:1556567867,ts_break:1557997096,ts_invert:1558682453,performance:2.4342518518,color:"hsl(276, 100%, 32%)"}, {id:103,name:"wizardly_allen",ts_publish:1564421435,ts_break:1565251735,ts_invert:1565251763,performance:6.9788554902,color:"hsl(146, 100%, 41%)"}, {id:106,name:"xenodochial_northcutt",ts_publish:1564481053,ts_break:1565035306,ts_invert:1565073545,performance:9.4707902241,color:"hsl(357, 100%, 63%)"}, {id:102,name:"blissful_fermi",ts_publish:1564406646,ts_break:1564937275,ts_invert:-1,performance:10.3321277854,color:"hsl(264, 100%, 57%)"}, {id:87,name:"eager_euler",ts_publish:1563697720,ts_break:1564300905,ts_invert:1564232221,performance:7.9275899407,color:"hsl(65, 100%, 32%)"}, {id:46,name:"dazzling_panini",ts_publish:1557935941,ts_break:1558511789,ts_invert:1558511742,performance:8.4520230556,color:"hsl(55, 100%, 30%)"}, {id:93,name:"brave_swanson",ts_publish:1564133118,ts_break:1565192157,ts_invert:1565192127,performance:2.4842031043,color:"hsl(185, 100%, 22%)"}, {id:82,name:"stoic_thompson",ts_publish:1560635878,ts_break:1561311560,ts_invert:1561139763,performance:6.0123038065,color:"hsl(74, 100%, 52%)"}, {id:27,name:"cranky_mccarthy",ts_publish:1555517823,ts_break:1556214599,ts_invert:1558964555,performance:5.5669203727,color:"hsl(215, 100%, 62%)"}, {id:31,name:"zealous_ardinghelli",ts_publish:1555673427,ts_break:1556028186,ts_invert:1556028169,performance:10.3609592233,color:"hsl(283, 100%, 49%)"}, {id:69,name:"hungry_elion",ts_publish:1559128309,ts_break:1559644843,ts_invert:-1,performance:1.6538476098,color:"hsl(226, 100%, 55%)"}, {id:24,name:"lucid_roentgen",ts_publish:1554645186,ts_break:1554776207,ts_invert:-1,performance:11.5321718449,color:"hsl(94, 100%, 27%)"}, {id:21,name:"elated_hodgkin",ts_publish:1554274427,ts_break:1554618246,ts_invert:1554618242,performance:1.6509255261,color:"hsl(268, 100%, 51%)"}, {id:18,name:"elegant_sinoussi",ts_publish:1553760580,ts_break:1554102585,ts_invert:1554102568,performance:1.6662852365,color:"hsl(141, 100%, 55%)"}, {id:50,name:"flamboyant_engelbart",ts_publish:1558373064,ts_break:1558522048,ts_invert:-1,performance:6.7562694142,color:"hsl(290, 100%, 53%)"}, {id:3,name:"hopeful_liskov",ts_publish:1553355281,ts_break:1553600572,ts_invert:1553600557,performance:1.6640131544,color:"hsl(192, 100%, 37%)"}, {id:47,name:"peaceful_williams",ts_publish:1557953285,ts_break:1558021358,ts_invert:-1,performance:19.6259913794,color:"hsl(241, 100%, 31%)"}, {id:20,name:"focused_gary",ts_publish:1553883228,ts_break:1554102657,ts_invert:1554102646,performance:1.6493611568,color:"hsl(58, 100%, 33%)"}, {id:17,name:"condescending_shockley",ts_publish:1553613133,ts_break:1553678138,ts_invert:-1,performance:11.4471859381,color:"hsl(242, 100%, 47%)"}, {id:22,name:"serene_aryabhata",ts_publish:1554307522,ts_break:1554365490,ts_invert:1554365434,performance:12.2491671319,color:"hsl(351, 100%, 58%)"}, {id:14,name:"goofy_archimedes",ts_publish:1553549586,ts_break:1553564301,ts_invert:-1,performance:18.6870436632,color:"hsl(64, 100%, 44%)"}, {id:38,name:"epic_dijkstra",ts_publish:1557199352,ts_break:1557216110,ts_invert:1562143763,performance:9.7638964132,color:"hsl(143, 100%, 25%)"}, {id:26,name:"distracted_leavitt",ts_publish:1554811435,ts_break:1554816131,ts_invert:-1,performance:18.4463197449,color:"hsl(137, 100%, 37%)"},  ];
	  return programs;
      }
</script>
<script src="/static/js/flot.js"></script>
