---
layout: base
title: Dashboard
edition: "2017"
---

  {% include index_boxes.html %}

  <hr>


  <div class="row">
    <div class="col-xs-12">
      <h2>Strawberry Scores</h2>
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
	  <div class="flot-plot flot-chart" data-flot="{{ site.data.plot | jsonify | xml_escape }}" style="height: 500px;"></div>
    </div>
  </div>

  <hr>

  <div class="row">
    <div class="col-xs-12">
      <h2>Banana Scores</h2>
	</div>
  </div>

  <div class="row">
    <div class="col-xs-12 col-lg-5">
	  <h3 id="bananas">Banana Ranking</h3>
	  {% include table_bananas_ranking.html %}
    </div>

    <div class="col-xs-12  col-lg-7">
	  <h3 id="breaks">All Challenge breaks</h3>
      {% include table_breaks.html %}
    </div>
  </div><!-- row -->
