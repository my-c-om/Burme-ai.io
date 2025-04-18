// threeScene.js
import * as THREE from 'https://cdn.skypack.dev/three@0.142.0';

let scene, camera, renderer, particles;

function init() {
  const container = document.getElementById("scene");

  // Scene Setup
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(
    75,
    container.clientWidth / container.clientHeight,
    0.1,
    1000
  );
  camera.position.z = 5;

  renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  renderer.setSize(container.clientWidth, container.clientHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  container.appendChild(renderer.domElement);

  // Particle Geometry
  const geometry = new THREE.BufferGeometry();
  const vertices = [];

  for (let i = 0; i < 1000; i++) {
    const x = THREE.MathUtils.randFloatSpread(10);
    const y = THREE.MathUtils.randFloatSpread(10);
    const z = THREE.MathUtils.randFloatSpread(10);
    vertices.push(x, y, z);
  }

  geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));

  const material = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 0.05,
    transparent: true,
    blending: THREE.AdditiveBlending
  });

  particles = new THREE.Points(geometry, material);
  scene.add(particles);

  animate();
}

function animate() {
  requestAnimationFrame(animate);

  particles.rotation.y += 0.0015;
  particles.rotation.x += 0.0008;

  renderer.render(scene, camera);
}

window.addEventListener('load', init);
window.addEventListener('resize', () => {
  const container = document.getElementById("scene");
  camera.aspect = container.clientWidth / container.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(container.clientWidth, container.clientHeight);
});
