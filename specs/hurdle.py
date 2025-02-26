from lucidsim import EXAMPLE_CHECKPOINTS_ROOT
from lucidsim.traj_samplers import unroll_flow_stream as unroll

gen = unroll.main(
    env_name="Hurdle",
    checkpoint=f"{EXAMPLE_CHECKPOINTS_ROOT}/expert.pt",
    vision_key=None,
    render=True,
    num_steps=500,
    seed=30,
    imagen_on=False,
)

for data in gen:
    pass
