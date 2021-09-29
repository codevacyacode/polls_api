var domain = 'https://murmuring-depths-65428.herokuapp.com/polls/'

window.onload = function() {
	var list = document.getElementById('list');
	
	var pollListLoader = new XMLHttpRequest()
	pollListLoader.onreadystatechange = function() {
		if (pollListLoader.readyState == 4) {
			if (pollListLoader.status == 200) {
				var data = JSON.parse(pollListLoader.responseText);
				var s = '<ul>';
				for (i = 0; i < data.length; i++) {
					s += '<li>' + data[i].title + '</li>';
				}
				s += '</ul>'
				list.innerHTML = s;
			}
		}
	}
	
	function pollListLoad() {
		pollListLoader.open('GET', domain + 'api/polls/', true);
		pollListLoader.send();
	}
	
	pollListLoad();
}