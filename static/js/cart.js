var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action

		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)


		if (user == 'AnonymousUser'){
			alert('Please Login');
			// addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function getShoeSize()
{
	var size = document.getElementById('shoeSize')
	value = size.options[size.selectedIndex].value
	return value
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

	
	var url = '/update_item/'
	size=getShoeSize()
	console.log('size',size)

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		}, 
		body:JSON.stringify({'productId':productId, 'action':action, 'size':size})
	})

	.then((response) => {
	   return response.json();
	})

	.then((data) => {
	    location.reload()
	});
}