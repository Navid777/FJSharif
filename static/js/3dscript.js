var scene, camera, renderer;
var Limbs = new Object();
var LimbsController = {
    Pelvic			: true,
    Right_Femur		: true,
    Right_Tibia		: true,
    Right_Fibula	: true,
    Right_Patella	: true,
    Left_Femur		: true,
    Left_Tibia		: true,
    Left_Fibula		: true,
    Left_Patella	: true
}
scene = new THREE.Scene();
initGUI();
init();
animate();

function init() {
    var WIDTH = window.innerWidth, HEIGHT = window.innerHeight;

    renderer = new THREE.WebGLRenderer({antialias:true});
    renderer.setSize(WIDTH, HEIGHT);
    document.getElementById('3d-canvas').appendChild(renderer.domElement);

    // camera = new THREE.PerspectiveCamera(45, WIDTH / HEIGHT, 0.1, 20000);
    camera = new THREE.OrthographicCamera( - WIDTH / 2, WIDTH / 2, HEIGHT / 2, -HEIGHT / 2, 0.1, 20000 );
    camera.position.set(0,0,600);
    scene.add(camera);

    // Create an event listener that resizes the renderer with the browser window.
    window.addEventListener('resize', function() 	{
        var WIDTH = window.innerWidth, HEIGHT = window.innerHeight;
        renderer.setSize(WIDTH, HEIGHT);
        camera.aspect = WIDTH / HEIGHT;
        camera.updateProjectionMatrix();   			});

    // Set the background color of the scene.
    renderer.setClearColor(0x333F47, 1);

    // Create a light, set its position, and add it to the scene.
    var light = new THREE.PointLight(0xffffff);
    light.position.set(-100,200,100);
    scene.add(light);

    CreateLimbs();
    UpdateLimbStatus();

    controls = new THREE.OrbitControls(camera, renderer.domElement);
}

function animate() {
    requestAnimationFrame(animate);

    renderer.render(scene, camera);
    controls.update();
}

function CreateLimbs(){
    var material = new THREE.MeshPhongMaterial( { color: 0xffff00, specular: 0xffff00, shininess: 20 } );

    var loader = new THREE.STLLoader();
    loader.load('http://localhost:8000/media/stl/MOHAMMAD_AKBAR_L3.stl', function ( geometry ) {
        var mesh = new THREE.Mesh( geometry, material );

        mesh.castShadow = true;
        mesh.receiveShadow = true;

        Limbs.Pelvic = mesh;
    } );

    var geometry = new THREE.BoxGeometry( 100, 100, 100 );
    //var material = new THREE.MeshBasicMaterial( { color: 0xffff00 } );

    var mesh = new THREE.Mesh( geometry, material );mesh.position.set(-300,0,0); Limbs.Right_Femur = mesh;
    var mesh = new THREE.Mesh( geometry, material );mesh.position.set(-200,0,0); Limbs.Right_Tibia = mesh;
    var mesh = new THREE.Mesh( geometry, material );mesh.position.set(-100,0,0); Limbs.Right_Fibula = mesh;
    var mesh = new THREE.Mesh( geometry, material );mesh.position.set(0,0,0); Limbs.Right_Patella = mesh;
    var mesh = new THREE.Mesh( geometry, material );mesh.position.set(100,0,0); Limbs.Left_Femur = mesh;
    var mesh = new THREE.Mesh( geometry, material );mesh.position.set(200,0,0); Limbs.Left_Tibia = mesh;
    var mesh = new THREE.Mesh( geometry, material );mesh.position.set(300,0,0); Limbs.Left_Fibula = mesh;
    var mesh = new THREE.Mesh( geometry, material );mesh.position.set(400,0,0); Limbs.Left_Patella = mesh;
}

function UpdateLimbStatus(){
    for(Limb in Limbs){
        if (LimbsController[Limb]==true){scene.add(Limbs[Limb]);}else{scene.remove(Limbs[Limb]);}
    }

}

function initGUI() {
    LimbsController.gui = new dat.GUI();

    var ShowPelvic = 		LimbsController.gui.addFolder( 'Pelvic' );
    var ShowRightLimbs = 	LimbsController.gui.addFolder( 'Right Leg' );
    var ShowLeftLimbs = 	LimbsController.gui.addFolder( 'Left Leg' );

    ShowPelvic.add( LimbsController, "Pelvic" ).onChange(function(value) {UpdateLimbStatus();});

    ShowRightLimbs.add( LimbsController, "Right_Femur" )	.name("Right Femur").onChange(function(value) {UpdateLimbStatus();});
    ShowRightLimbs.add( LimbsController, "Right_Tibia" )	.name("Right Tibia").onChange(function(value) {UpdateLimbStatus();});;
    ShowRightLimbs.add( LimbsController, "Right_Fibula" )	.name("Right Fibula").onChange(function(value) {UpdateLimbStatus();});;
    ShowRightLimbs.add( LimbsController, "Right_Patella" )	.name("Right_Patella").onChange(function(value) {UpdateLimbStatus();});;

    ShowLeftLimbs.add( LimbsController, "Left_Femur" )		.name("Left Femur").onChange(function(value) {UpdateLimbStatus();});;
    ShowLeftLimbs.add( LimbsController, "Left_Tibia" )		.name("Left Tibia").onChange(function(value) {UpdateLimbStatus();});;
    ShowLeftLimbs.add( LimbsController, "Left_Fibula" )		.name("Left Fibula").onChange(function(value) {UpdateLimbStatus();});;
    ShowLeftLimbs.add( LimbsController, "Left_Patella" )	.name("Left Patella").onChange(function(value) {UpdateLimbStatus();});;

    ShowPelvic.open();
    ShowRightLimbs.open();
    ShowLeftLimbs.open();
}