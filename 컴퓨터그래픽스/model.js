Model = {};

Model.torso = function() {
	var geometry = new THREE.Geometry();
	geometry.vertices.push(
		new THREE.Vector3(-3, -1, -1),
		new THREE.Vector3(3, -1, -1),
		new THREE.Vector3(-3, 1, -1),
		new THREE.Vector3(3, 1, -1),
		new THREE.Vector3(-3, -1, 1),
		new THREE.Vector3(3, -1, 1),
		new THREE.Vector3(-3, 1, 1),
		new THREE.Vector3(3, 1, 1)
	);
	geometry.faces.push(
		// 앞면
		new THREE.Face3(0, 3, 2),
		new THREE.Face3(0, 1, 3),
		// 윗면
		new THREE.Face3(2, 7, 6),
		new THREE.Face3(2, 3, 7),
		// 뒷면
		new THREE.Face3(6, 5, 4),
		new THREE.Face3(6, 7, 5),
		// 아랫면
		new THREE.Face3(4, 1, 0),
		new THREE.Face3(4, 5, 1),
		// 옆면(왼쪽)
		new THREE.Face3(4, 2, 6),
		new THREE.Face3(4, 0, 2),
		// 옆면(오른쪽)
		new THREE.Face3(1, 7, 3),
		new THREE.Face3(1, 5, 7)	
	);
	var material = new THREE.MeshLambertMaterial( {color: 0xF7FE2E} );
	var torso = new THREE.Mesh(geometry, material);
	return torso;
}

Model.head = function() {
	var geometry = new THREE.IcosahedronGeometry(1.5);
	var material = new THREE.MeshLambertMaterial( {color: 0xF7FE2E} );
	var head = new THREE.Mesh(geometry, material);
	head.position.set(-3.5, 1.5, 0);
	return head;
}

Model.upLeg = function() {
	var geometry = new THREE.Geometry();
	geometry.vertices.push(
		new THREE.Vector3(-0.5, -1.5, 0.5),
		new THREE.Vector3(0.5, -1.5, 0.5),
		new THREE.Vector3(-0.5, 0, 0.5),
		new THREE.Vector3(0.5, 0, 0.5),
		new THREE.Vector3(-0.5, -1.5, 0),
		new THREE.Vector3(0.5, -1.5, 0),
		new THREE.Vector3(-0.5, 0, 0),
		new THREE.Vector3(0.5, 0, 0)
	);
	geometry.faces.push(
		// 앞면
		new THREE.Face3(0, 3, 2),
		new THREE.Face3(0, 1, 3),
		// 윗면
		new THREE.Face3(2, 7, 6),
		new THREE.Face3(2, 3, 7),
		// 뒷면
		new THREE.Face3(6, 5, 4),
		new THREE.Face3(6, 7, 5),
		// 아랫면
		new THREE.Face3(4, 1, 0),
		new THREE.Face3(4, 5, 1),
		// 옆면(왼쪽)
		new THREE.Face3(4, 2, 6),
		new THREE.Face3(4, 0, 2),
		// 옆면(오른쪽)
		new THREE.Face3(1, 7, 3),
		new THREE.Face3(1, 5, 7)
	);
	var material = new THREE.MeshLambertMaterial( {color: 0xF7FE2E} );
	var leftFrontUpLeg = new THREE.Mesh(geometry, material);	
	return leftFrontUpLeg;
}

Model.downLeg = function() {
	var geometry = new THREE.Geometry();
	geometry.vertices.push(
		new THREE.Vector3(-0.5, -3, 0.5),
		new THREE.Vector3(0.5, -3, 0.5),
		new THREE.Vector3(-0.5, -1.5, 0.5),
		new THREE.Vector3(0.5, -1.5, 0.5),
		new THREE.Vector3(-0.5, -3, 0),
		new THREE.Vector3(0.5, -3, 0),
		new THREE.Vector3(-0.5, -1.5, 0),
		new THREE.Vector3(0.5, -1.5, 0)
	);
	geometry.faces.push(
		// 앞면
		new THREE.Face3(0, 3, 2),
		new THREE.Face3(0, 1, 3),
		// 윗면
		new THREE.Face3(2, 7, 6),
		new THREE.Face3(2, 3, 7),
		// 뒷면
		new THREE.Face3(6, 5, 4),
		new THREE.Face3(6, 7, 5),
		// 아랫면
		new THREE.Face3(4, 1, 0),
		new THREE.Face3(4, 5, 1),
		// 옆면(왼쪽)
		new THREE.Face3(4, 2, 6),
		new THREE.Face3(4, 0, 2),
		// 옆면(오른쪽)
		new THREE.Face3(1, 7, 3),
		new THREE.Face3(1, 5, 7)
	);
	var material = new THREE.MeshLambertMaterial( {color: 0xF7FE2E} );
	var leftFrontDownLeg = new THREE.Mesh(geometry, material);
	return leftFrontDownLeg;
}


Model.upTail = function() {
	var geometry = new THREE.Geometry();
	geometry.vertices.push(
		new THREE.Vector3(0, 0, 0.2),
		new THREE.Vector3(1, 0, 0.2),
		new THREE.Vector3(0, 0.5, 0.2),
		new THREE.Vector3(1, 0.5, 0.2),
		new THREE.Vector3(0, 0, -0.2),
		new THREE.Vector3(1, 0, -0.2),
		new THREE.Vector3(0, 0.5, -0.2),
		new THREE.Vector3(1, 0.5, -0.2)
	);
	geometry.faces.push(
		// 앞면
		new THREE.Face3(0, 3, 2),
		new THREE.Face3(0, 1, 3),
		// 윗면
		new THREE.Face3(2, 7, 6),
		new THREE.Face3(2, 3, 7),
		// 뒷면
		new THREE.Face3(6, 5, 4),
		new THREE.Face3(6, 7, 5),
		// 아랫면
		new THREE.Face3(4, 1, 0),
		new THREE.Face3(4, 5, 1),
		// 옆면(왼쪽)
		new THREE.Face3(4, 2, 6),
		new THREE.Face3(4, 0, 2),
		// 옆면(오른쪽)
		new THREE.Face3(1, 7, 3),
		new THREE.Face3(1, 5, 7)
	);
	var material = new THREE.MeshLambertMaterial( {color: 0xF7FE2E} );
	var upTail = new THREE.Mesh(geometry, material);
	return upTail;
}

Model.downTail = function() {
	var geometry = new THREE.Geometry();
	geometry.vertices.push(
		new THREE.Vector3(1, 0, 0.2),
		new THREE.Vector3(2, 0, 0.2),
		new THREE.Vector3(1, 0.5, 0.2),
		new THREE.Vector3(2, 0.5, 0.2),
		new THREE.Vector3(1, 0, -0.2),
		new THREE.Vector3(2, 0, -0.2),
		new THREE.Vector3(1, 0.5, -0.2),
		new THREE.Vector3(2, 0.5, -0.2)
	);
	geometry.faces.push(
		// 앞면
		new THREE.Face3(0, 3, 2),
		new THREE.Face3(0, 1, 3),
		// 윗면
		new THREE.Face3(2, 7, 6),
		new THREE.Face3(2, 3, 7),
		// 뒷면
		new THREE.Face3(6, 5, 4),
		new THREE.Face3(6, 7, 5),
		// 아랫면
		new THREE.Face3(4, 1, 0),
		new THREE.Face3(4, 5, 1),
		// 옆면(왼쪽)
		new THREE.Face3(4, 2, 6),
		new THREE.Face3(4, 0, 2),
		// 옆면(오른쪽)
		new THREE.Face3(1, 7, 3),
		new THREE.Face3(1, 5, 7)
	);
	var material = new THREE.MeshLambertMaterial( {color: 0xF7FE2E} );
	var downTail = new THREE.Mesh(geometry, material);
	return downTail;
}