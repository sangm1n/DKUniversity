var scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);
var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

var controls = new THREE.OrbitControls(camera);
controls.update();

// torso
var torso = Model.torso();
scene.add(torso);

// head
var head = Model.head();
scene.add(head);

// front leg
var leftFrontUpLeg = Model.upLeg();
scene.add(leftFrontUpLeg);
var leftFrontDownLeg = Model.downLeg();
scene.add(leftFrontDownLeg);
var rightFrontUpLeg = Model.upLeg();
scene.add(rightFrontUpLeg);
var rightFrontDownLeg = Model.downLeg();
scene.add(rightFrontDownLeg);

// back leg
var leftBackUpLeg = Model.upLeg();
scene.add(leftBackUpLeg);
var leftBackDownLeg = Model.downLeg();
scene.add(leftBackDownLeg);
var rightBackUpLeg = Model.upLeg();
scene.add(rightBackUpLeg);
var rightBackDownLeg = Model.downLeg();
scene.add(rightBackDownLeg);

// tail
var upTail = Model.upTail();
scene.add(upTail);
var downTail = Model.downTail();
scene.add(downTail);

camera.position.z = 10;

head.position.set(-3, 1.5, 0);
var headIdx = 0;

leftFrontUpLeg.position.set(-1.5, 0.5, 1);
leftFrontDownLeg.position.set(-1.5, 0.5, 1);
var leftFrontUpLegIdx = 0;
var leftFrontDownLegIdx = 0;

leftBackUpLeg.position.set(1.5, 0.5, 1);
leftBackDownLeg.position.set(1.5, 0.5, 1);
var leftBackUpLegIdx = 0;
var leftBackDownLegIdx = 0;

rightFrontUpLeg.position.set(-1.5, 0.5, -1.5);
rightFrontDownLeg.position.set(-1.5, 0.5, -1.5);
var rightFrontUpLegIdx = 0;
var rightFrontDownLegIdx = 0;

rightBackUpLeg.position.set(1.5, 0.5, -1.5);
rightBackDownLeg.position.set(1.5, 0.5, -1.5);
var rightBackUpLegIdx = 0;
var rightBackDownLegIdx = 0;

upTail.position.set(3, 0.5, 0);
downTail.position.set(3, 0.5, 0);
var upTailIdx = 0;
var downTailIdx = 0;

var light = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(light);
var light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(-5, 5, 2)
scene.add(light);

var render = function() {
	requestAnimationFrame(render);
	controls.update();
	renderer.render(scene, camera);
};

render();