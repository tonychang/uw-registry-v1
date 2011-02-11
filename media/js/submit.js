google.setOnLoadCallback(
    function() {
        $("input[name='in_development']").click(function() {
		            $("input[name='doc_url']").toggle(this.checked);
		  }
    });