#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution; 

float circleShape(float radius, vec2 position){
    return step(radius, length(position-vec2(0.5)));

}

void main(){
    vec2 coord = gl_FragCoord.xy / u_resolution;
    vec3 color = vec3(0.0);

    vec2 translate = vec2(0.1, 0.0);
    coord += translate * 0.5;
    color += vec3(circleShape(0.3, coord));
    gl_FragColor = vec4(color, 1.0);
}