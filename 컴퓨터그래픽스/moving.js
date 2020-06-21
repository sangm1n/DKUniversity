var moveHead = function() {
	requestAnimationFrame(moveHead);

	if (headIdx == 0) {
		head.rotateY(-0.02);

		if (head.rotation.y < -0.5)
			headIdx = 1;
	}

	else {
		head.rotateY(+0.02);

		if (head.rotation.y > 0.5)
			headIdx = 0;
	}

	controls.update();
	renderer.render(scene, camera);
}

var moveLeftFrontLeg = function() {
	requestAnimationFrame(moveLeftFrontLeg);

	if (leftFrontUpLegIdx == 0) {
		leftFrontUpLeg.rotateZ(-0.03);
		leftFrontDownLeg.rotateZ(-0.03);
		if (leftFrontDownLegIdx == 0) {
			leftFrontDownLeg.rotateZ(-0.015);

			if (leftFrontUpLeg.rotation.z < -0.3) {
				leftFrontDownLegIdx = 1;
			}
		}
		else {
			leftFrontDownLeg.rotateZ(+0.015);

			if (leftFrontUpLeg.rotation.z > 0.3) {
				leftFrontDownLegIdx = 0;
			}
		}
		
		if (leftFrontUpLeg.rotation.z < -0.5) {
			leftFrontUpLegIdx = 1;
		}
	}

	else {
		leftFrontUpLeg.rotateZ(+0.03);
		leftFrontDownLeg.rotateZ(+0.03);
		if (leftFrontDownLegIdx == 0) {
			leftFrontDownLeg.rotateZ(-0.015);

			if (leftFrontUpLeg.rotation.z < -0.3) {
				leftFrontDownLegIdx = 1;
			}
		}
		else {
			leftFrontDownLeg.rotateZ(+0.015);

			if (leftFrontUpLeg.rotation.z > 0.3) {
				leftFrontDownLegIdx = 0;
			}
		}
		
		if (leftFrontUpLeg.rotation.z > 0.5) {
			leftFrontUpLegIdx = 0;
		}
	}

	controls.update();
	renderer.render(scene, camera);
}

var moveLeftBackLeg = function() {
	requestAnimationFrame(moveLeftBackLeg);

	if (leftBackUpLegIdx == 0) {
		leftBackUpLeg.rotateZ(-0.03);
		leftBackDownLeg.rotateZ(-0.03);
		if (leftBackDownLegIdx == 0) {
			leftBackDownLeg.rotateZ(-0.015);

			if (leftBackUpLeg.rotation.z < -0.3) {
				leftBackDownLegIdx = 1;
			}
		}
		else {
			leftBackDownLeg.rotateZ(+0.015);

			if (leftBackUpLeg.rotation.z > 0.3) {
				leftBackDownLegIdx = 0;
			}
		}
		
		if (leftBackUpLeg.rotation.z < -0.5) {
			leftBackUpLegIdx = 1;
		}
	}

	else {
		leftBackUpLeg.rotateZ(+0.03);
		leftBackDownLeg.rotateZ(+0.03);
		if (leftBackDownLegIdx == 0) {
			leftBackDownLeg.rotateZ(-0.015);

			if (leftBackUpLeg.rotation.z < -0.3) {
				leftBackDownLegIdx = 1;
			}
		}
		else {
			leftBackDownLeg.rotateZ(+0.015);

			if (leftBackUpLeg.rotation.z > 0.3) {
				leftBackDownLegIdx = 0;
			}
		}
		
		if (leftBackUpLeg.rotation.z > 0.5) {
			leftBackUpLegIdx = 0;
		}
	}

	controls.update();
	renderer.render(scene, camera);
}

var moveRightFrontLeg = function() {
	requestAnimationFrame(moveRightFrontLeg);

	if (rightFrontUpLegIdx == 0) {
		rightFrontUpLeg.rotateZ(-0.03);
		rightFrontDownLeg.rotateZ(-0.03);
		if (rightFrontDownLegIdx == 0) {
			rightFrontDownLeg.rotateZ(-0.015);

			if (rightFrontUpLeg.rotation.z < -0.3) {
				rightFrontDownLegIdx = 1;
			}
		}
		else {
			rightFrontDownLeg.rotateZ(+0.015);

			if (rightFrontUpLeg.rotation.z > 0.3) {
				rightFrontDownLegIdx = 0;
			}
		}
		
		if (rightFrontUpLeg.rotation.z < -0.5) {
			rightFrontUpLegIdx = 1;
		}
	}

	else {
		rightFrontUpLeg.rotateZ(+0.03);
		rightFrontDownLeg.rotateZ(+0.03);
		if (rightFrontDownLegIdx == 0) {
			rightFrontDownLeg.rotateZ(-0.015);

			if (rightFrontUpLeg.rotation.z < -0.3) {
				rightFrontDownLegIdx = 1;
			}
		}
		else {
			rightFrontDownLeg.rotateZ(+0.015);

			if (rightFrontUpLeg.rotation.z > 0.3) {
				rightFrontDownLegIdx = 0;
			}
		}
		
		if (rightFrontUpLeg.rotation.z > 0.5) {
			rightFrontUpLegIdx = 0;
		}
	}

	controls.update();
	renderer.render(scene, camera);
}

var moveRightBackLeg = function() {
	requestAnimationFrame(moveRightBackLeg);

	if (rightBackUpLegIdx == 0) {
		rightBackUpLeg.rotateZ(-0.03);
		rightBackDownLeg.rotateZ(-0.03);
		if (rightBackDownLegIdx == 0) {
			rightBackDownLeg.rotateZ(-0.015);

			if (rightBackUpLeg.rotation.z < -0.3) {
				rightBackDownLegIdx = 1;
			}
		}
		else {
			rightBackDownLeg.rotateZ(+0.015);

			if (rightBackUpLeg.rotation.z > 0.3) {
				rightBackDownLegIdx = 0;
			}
		}
		
		if (rightBackUpLeg.rotation.z < -0.5) {
			rightBackUpLegIdx = 1;
		}
	}

	else {
		rightBackUpLeg.rotateZ(+0.03);
		rightBackDownLeg.rotateZ(+0.03);
		if (rightBackDownLegIdx == 0) {
			rightBackDownLeg.rotateZ(-0.015);

			if (rightBackUpLeg.rotation.z < -0.3) {
				rightBackDownLegIdx = 1;
			}
		}
		else {
			rightBackDownLeg.rotateZ(+0.015);

			if (rightBackUpLeg.rotation.z > 0.3) {
				rightBackDownLegIdx = 0;
			}
		}
		
		if (rightBackUpLeg.rotation.z > 0.5) {
			rightBackUpLegIdx = 0;
		}
	}

	controls.update();
	renderer.render(scene, camera);
}

var moveTail = function() {
	requestAnimationFrame(moveTail);
	
	if (upTailIdx == 0) {
		upTail.rotateZ(-0.03);
		downTail.rotateZ(-0.03);
		if (downTailIdx == 0) {
			downTail.rotateY(-0.02);

			if (downTail.rotation.y < -0.25) {
				downTailIdx = 1;
			}
		}
		else {
			downTail.rotateY(+0.02);

			if (downTail.rotation.y > 0.25) {
				downTailIdx = 0;
			}
		}

		if (upTail.rotation.z < -0.8) {
			upTailIdx = 1;
		}
	}

	else {
		upTail.rotateZ(+0.03);
		downTail.rotateZ(+0.03);
		if (downTailIdx == 0) {
			downTail.rotateY(-0.02);

			if (downTail.rotation.y < -0.25) {
				downTailIdx = 1;
			}
		}
		else {
			downTail.rotateY(+0.02);

			if (downTail.rotation.y > 0.25) {
				downTailIdx = 0;
			}
		}

		if (upTail.rotation.z > 0.8) {
			upTailIdx = 0;
		}
	}

	controls.update();
	renderer.render(scene, camera);
}