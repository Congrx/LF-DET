import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--angRes", type=int, default=5, help="angular resolution")
parser.add_argument("--patch_size", type=int, default=32, help="patch size for train")
parser.add_argument("--scale_factor", type=int, default=4, help="4, 2")
parser.add_argument('--model_name', type=str, default='LF-DET', help="model name")
parser.add_argument("--channels", type=int, default=64, help="channels , embed_dim for transformer —— C")
parser.add_argument("--ang_num_heads", type=int, default=4, help="number of multi heads for angular transformer —— P")
parser.add_argument("--spa_num_heads", type=int, default=4, help="number of multi heads for spatial transformer —— P")
parser.add_argument("--ang_mlp_ratio", type=int, default=4, help="scale ratio in MLP for angular transformer")
parser.add_argument("--spa_mlp_ratio", type=int, default=4, help="scale ratio in MLP for spatial transformer")
parser.add_argument("--depth", type=int, default=4, help="number of spatial-angular transformer encoder —— N")
parser.add_argument("--ang_sr_ratio", type=int, default=1, help="reduce patches scale for angular transformer")
parser.add_argument("--spa_sr_ratio", type=int, default=2, help="reduce patches scale for spatial transformer —— S")
parser.add_argument("--spa_trans_num", type=int, default=2, help="number of spatial transformer in transformer encoder —— K")
parser.add_argument("--attn_drop_rate", type=float, default=0.0, help="drop rate for attention calculation")
parser.add_argument("--drop_rate", type=float, default=0.0, help="common drop rate")
parser.add_argument("--drop_path_rate", type=float, default=0.1, help="stochastic depth decay rule")
parser.add_argument("--use_pre_ckpt", type=bool, default=True, help="use pre model ckpt")
parser.add_argument("--path_pre_pth", type=str, default='./pretrain/LF_DET_5x5_4x_epoch_90_model.pth',
                    help="path for pre model ckpt")
parser.add_argument('--data_name', type=str, default='ALL',
                    help='EPFL, HCI_new, HCI_old, INRIA_Lytro, Stanford_Gantry, ALL')
parser.add_argument('--path_for_train', type=str, default='../datasets/train/')
parser.add_argument('--path_for_test', type=str, default='../BasicLFSR-main/data_for_test/')
parser.add_argument('--path_log', type=str, default='./log')
parser.add_argument('--patch_size_for_test', default=32, type=int, help='patch size')
parser.add_argument('--stride_for_test', default=16, type=int, help='stride')
parser.add_argument('--batch_size', type=int, default=3)
parser.add_argument('--lr', type=float, default=2.5e-4, help='initial learning rate')
parser.add_argument('--decay_rate', type=float, default=0, help='weight decay [default: 1e-4]')
parser.add_argument('--n_steps', type=int, default=15, help='number of epochs to update learning rate')
parser.add_argument('--gamma', type=float, default=0.5, help='gamma')
parser.add_argument('--epoch', default=90, type=int, help='Epoch to run [default: 90]')
parser.add_argument('--device', type=str, default='cuda:0')
parser.add_argument('--num_workers', type=int, default=2, help='num workers of the Data Loader')
parser.add_argument('--local_rank', dest='local_rank', type=int, default=0, )

args = parser.parse_args()
# parameters for test
args.patch_size_for_test = 32
args.stride_for_test = 16
args.minibatch_for_test = 2
