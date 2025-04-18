// threeScene.js ကို ဒီလိုစတင်ပါ
import * as THREE from 'three';

// 1. Scene Setup
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0f172a);

// 2. Add Floating Particles
const particles = new THREE.BufferGeometry();
const particleCount = 2000;
const posArray = new Float32Array(particleCount * 3);

for(let i = 0; i < particleCount * 3; i++) {
  posArray[i] = (Math.random() - 0.5) * 10;
}

particles.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
const particleMaterial = new THREE.PointsMaterial({
  size: 0.03,
  color: 0xffffff,
  transparent: true,
  opacity: 0.8
});

const particleMesh = new THREE.Points(particles, particleMaterial);
scene.add(particleMesh);

// 3. Animation Loop
function animate() {
  requestAnimationFrame(animate);
  particleMesh.rotation.x += 0.0005;
  particleMesh.rotation.y += 0.0007;
  renderer.render(scene, camera);
}
animate();
