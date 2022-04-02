from ... import utils
from ..OP_XB.xbs_to_ob import xbs_to_ob


def get_nmult(ob):
    """!
    Get number of MULT multiply
    """
    if not ob.bf_mult_export:
        return 1
    fake_xbs, _ = multiply_xbs(
        xbs=tuple((tuple((0.0, 0.0, 0.0, 0.0, 0.0, 0.0)),)), hids=tuple(("",)), ob=ob
    )
    return len(fake_xbs)


def multiply_xbs(xbs, hids, ob):
    """!
    Return lists of xb and their hid as multiplied by FDS MULT from ob.
    """
    # Init
    if not hids:
        hids = list(("",)) * len(xbs)
    export = ob.bf_mult_export
    # Calc, fast track
    if not export:
        return xbs, hids
    # Init the rest
    dxb = ob.bf_mult_dxb
    d = (ob.bf_mult_dx, ob.bf_mult_dy, ob.bf_mult_dz)
    d0 = (ob.bf_mult_dx0, ob.bf_mult_dy0, ob.bf_mult_dz0)
    lower = (
        ob.bf_mult_i_lower,
        ob.bf_mult_j_lower,
        ob.bf_mult_k_lower,
        ob.bf_mult_n_lower,
    )
    lower_skip = (
        ob.bf_mult_i_lower_skip,
        ob.bf_mult_j_lower_skip,
        ob.bf_mult_k_lower_skip,
        ob.bf_mult_n_lower_skip,
    )
    upper = (
        ob.bf_mult_i_upper,
        ob.bf_mult_j_upper,
        ob.bf_mult_k_upper,
        ob.bf_mult_n_upper,
    )
    upper_skip = (
        ob.bf_mult_i_upper_skip,
        ob.bf_mult_j_upper_skip,
        ob.bf_mult_k_upper_skip,
        ob.bf_mult_n_upper_skip,
    )
    # Calc, slow track
    multi_xbs, multi_hids = list(), list()
    for xb, hid in zip(xbs, hids):
        new_xbs, new_hids = multiply_xb(
            xb,
            hid,
            dxb,
            d,  # dx,dy,dz
            d0,  # dx0,dy0,dz0,
            lower,  # i,j,k,n
            lower_skip,  # i,j,k,n
            upper,  # i,j,k,n
            upper_skip,
        )
        multi_xbs.extend(new_xbs)
        multi_hids.extend(new_hids)
    return multi_xbs, multi_hids


def multiply_xb(
    xb,
    hid,
    dxb,
    d,  # dx,dy,dz
    d0,  # dx0,dy0,dz0,
    lower,  # i,j,k,n
    lower_skip,  # i,j,k,n
    upper,  # i,j,k,n
    upper_skip,  # i,j,k,n
):
    """!
    Return lists of xb and their hid as multiplied by FDS MULT.
    """
    xbs, hids = list(), list()
    dx, dy, dz = d
    dx0, dy0, dz0 = d0
    i_lower, j_lower, k_lower, n_lower = lower
    i_lower_skip, j_lower_skip, k_lower_skip, n_lower_skip = lower_skip
    i_upper, j_upper, k_upper, n_upper = upper
    i_upper_skip, j_upper_skip, k_upper_skip, n_upper_skip = upper_skip
    has_skip = False
    if any(dxb):
        # N, DXB: OBST MULT example
        if n_lower_skip >= n_lower or n_upper_skip <= n_upper:
            has_skip = True
        for n in range(n_lower, n_upper + 1):
            if has_skip and n_lower_skip <= n <= n_upper_skip:
                continue
            xbs.append(
                (
                    xb[0] + dx0 + n * dxb[0],
                    xb[1] + dx0 + n * dxb[1],
                    xb[2] + dy0 + n * dxb[2],
                    xb[3] + dy0 + n * dxb[3],
                    xb[4] + dz0 + n * dxb[4],
                    xb[5] + dz0 + n * dxb[5],
                )
            )
            hids.append(f"{hid}_{n}")
    else:
        # I,J,K: MESH refining example
        if (
            i_lower_skip >= i_lower
            or j_lower_skip >= j_lower
            or k_lower_skip >= k_lower
            or i_upper_skip <= i_upper
            or j_upper_skip <= j_upper
            or k_upper_skip <= k_upper
        ):
            has_skip = True
        i_lower_skip = max(i_lower, i_lower_skip)
        for i in range(i_lower, i_upper + 1):
            for j in range(j_lower, j_upper + 1):
                for k in range(k_lower, k_upper + 1):
                    if has_skip and (
                        i_lower_skip <= i <= i_upper_skip
                        and j_lower_skip <= j <= j_upper_skip
                        and k_lower_skip <= k <= k_upper_skip
                    ):
                        continue
                    xbs.append(
                        (
                            xb[0] + dx0 + i * dx,
                            xb[1] + dx0 + i * dx,
                            xb[2] + dy0 + j * dy,
                            xb[3] + dy0 + j * dy,
                            xb[4] + dz0 + k * dz,
                            xb[5] + dz0 + k * dz,
                        )
                    )
                    hids.append(f"{hid}_i{i}_j{j}_k{k}")
    return xbs, hids


# def multiply_object(context, ob, ps):
#     """!
#     Multiply Object by FDS MULT parameters.
#     """
#     hids, xbs = mult_xb_to_xbs(
#         xb=utils.geometry.get_bbox_xb(context, ob=ob, world=True),
#         hid=ob.name,
#         dxb=ps["DXB"],
#         dx=ps["DX"],
#         dx0=ps["DX0"],
#         dy=ps["DY"],
#         dy0=ps["DY0"],
#         dz=ps["DZ"],
#         dz0=ps["DZ0"],
#         i_lower=ps["I_LOWER"],
#         i_lower_skip=ps["I_LOWER_SKIP"],
#         i_upper=ps["I_UPPER"],
#         i_upper_skip=ps["I_UPPER_SKIP"],
#         j_lower=ps["J_LOWER"],
#         j_lower_skip=ps["J_LOWER_SKIP"],
#         j_upper=ps["J_UPPER"],
#         j_upper_skip=ps["J_UPPER_SKIP"],
#         k_lower=ps["K_LOWER"],
#         k_lower_skip=ps["K_LOWER_SKIP"],
#         k_upper=ps["K_UPPER"],
#         k_upper_skip=ps["K_UPPER_SKIP"],
#         n_lower=ps["N_LOWER"],
#         n_lower_skip=ps["N_LOWER_SKIP"],
#         n_upper=ps["N_UPPER"],
#         n_upper_skip=ps["N_UPPER_SKIP"],
#     )
#     obs_new = list((ob,))  # add original
#     co = ob.users_collection[0]
#     # Make copies
#     for i in range(len(xbs) - 1):
#         ob_new = ob.copy()
#         ob_new.data = ob.data.copy()
#         co.objects.link(ob_new)
#         obs_new.append(ob_new)
#     # Set their bbox
#     for i, ob_new in enumerate(obs_new):
#         ob_new.name = hids[i]
#         xbs_to_ob(
#             context,
#             ob=ob_new,
#             xbs=xbs[i : i + 1],
#             bf_xb="BBOX",
#             set_origin=True,
#         )

# def mult_xb_to_xbs_orig(
#     xb,
#     hid,
#     dxb,
#     dx,
#     dx0,
#     dy,
#     dy0,
#     dz,
#     dz0,
#     i_lower,
#     i_lower_skip,
#     i_upper,
#     i_upper_skip,
#     j_lower,
#     j_lower_skip,
#     j_upper,
#     j_upper_skip,
#     k_lower,
#     k_lower_skip,
#     k_upper,
#     k_upper_skip,
#     n_lower,
#     n_lower_skip,
#     n_upper,
#     n_upper_skip,
# ):
#     hids, xbs = list(), list()
#     if n_lower or n_upper:
#         # Check skip
#         has_skip = n_lower_skip is not None or n_upper_skip is not None
#         if n_lower_skip is None:
#             n_lower_skip = n_lower
#         if n_upper_skip is None:
#             n_upper_skip = n_upper
#         # Build
#         for n in range(n_lower, n_upper + 1):
#             if has_skip and n_lower_skip <= n <= n_upper_skip:
#                 continue
#             hids.append(f"{hid}_{n}")
#             xbs.append(
#                 (
#                     xb[0] + dx0 + n * dxb[0],
#                     xb[1] + dx0 + n * dxb[1],
#                     xb[2] + dy0 + n * dxb[2],
#                     xb[3] + dy0 + n * dxb[3],
#                     xb[4] + dz0 + n * dxb[4],
#                     xb[5] + dz0 + n * dxb[5],
#                 )
#             )
#     else:  # mesh refining example
#         # Check skip
#         has_skip = True
#         if all(
#             x is None
#             for x in (
#                 i_lower_skip,
#                 i_upper_skip,
#                 j_lower_skip,
#                 j_upper_skip,
#                 k_lower_skip,
#                 k_upper_skip,
#             )
#         ):
#             has_skip = False
#         if i_lower_skip is None:
#             i_lower_skip = i_lower  # FIXME why not i_upper + 1? or 999
#         if i_upper_skip is None:
#             i_upper_skip = i_upper
#         if j_lower_skip is None:
#             j_lower_skip = j_lower
#         if j_upper_skip is None:
#             j_upper_skip = j_upper
#         if k_lower_skip is None:
#             k_lower_skip = k_lower
#         if k_upper_skip is None:
#             k_upper_skip = k_upper
#         # Build
#         for i in range(i_lower, i_upper + 1):
#             for j in range(j_lower, j_upper + 1):
#                 for k in range(k_lower, k_upper + 1):
#                     if has_skip and (
#                         i_lower_skip <= i <= i_upper_skip
#                         and j_lower_skip <= j <= j_upper_skip
#                         and k_lower_skip <= k <= k_upper_skip
#                     ):
#                         continue
#                     hids.append(f"{hid}_{i}_{j}_{k}")
#                     xbs.append(
#                         (
#                             xb[0] + dx0 + i * dx,
#                             xb[1] + dx0 + i * dx,
#                             xb[2] + dy0 + j * dy,
#                             xb[3] + dy0 + j * dy,
#                             xb[4] + dz0 + k * dz,
#                             xb[5] + dz0 + k * dz,
#                         )
#                     )
#     return hids, xbs
