import itertools
import dataset
import matplotlib.pyplot as plt


def plot_cpu_gpu_performance(file_path, bar_width=0.1, bar_space=0.01, group_space=0.5, fig_size=(8, 4),
                             font_size=15, style='seaborn-v0_8-whitegrid'):
    groups = [15, 15, 14, 12]
    offsets = list(itertools.accumulate([0] + groups))
    table = [line.replace("\n", "").replace(" ", "").split(",") for line in open(file_path, "r").readlines()]

    for i, group in enumerate(groups):
        df = table[offsets[i]:offsets[i + 1]]
        algo = df[0][0]
        timings = df[2:]

        gb = list()
        gr = list()
        sp = list()
        graphs = list()

        for t in timings:
            graphs.append(dataset.GRAPHS_NAMES_SHORT[t[0]])
            lg = float(t[3])
            gb.append(lg / float(t[1]) if t[1] != 'none' else 0)
            gr.append(lg / float(t[2]))
            sp.append(lg / float(t[4]))

        br1 = list(map(lambda x: group_space * x, range(len(gb))))
        br2 = [x + bar_width + bar_space for x in br1]
        br3 = [x + bar_width + bar_space for x in br2]

        plt.style.use(style)
        plt.figure(figsize=fig_size, tight_layout=True)

        plt.bar(br1, gb, width=bar_width, label='GraphBLAST')
        plt.bar(br2, gr, width=bar_width, label='Gunrock')
        plt.bar(br3, sp, width=bar_width, label='Spla')

        plt.xlabel('Graph', fontweight='bold', fontsize=font_size)
        plt.ylabel('Speed-up over LaGraph', fontweight='bold', fontsize=font_size)
        plt.xticks(list(map(lambda x: group_space * x + bar_width + bar_space, range(len(gb)))), graphs,
                   fontsize=font_size * 0.8, rotation=20)
        plt.yscale('log')

        plt.legend()
        plt.savefig(f"rq1_rel_{algo}.pdf", format="pdf")


def plot_gpu_n_core_performance(file_path, bar_width=0.1, bar_space=0.01, group_space=0.5, fig_size=(8, 4),
                                font_size=15, style='seaborn-v0_8-whitegrid'):
    groups = [15, 15, 14, 12]
    offsets = list(itertools.accumulate([0] + groups))
    table = [line.replace("\n", "").replace(" ", "").split(",") for line in open(file_path, "r").readlines()]

    for i, group in enumerate(groups):
        df = table[offsets[i]:offsets[i + 1]]
        algo = df[0][0]
        timings = df[2:]

        intel = list()
        amd = list()
        nvidia = list()
        graphs = list()

        for t in timings:
            nnz = dataset.GRAPHS_DATA[t[0]].size
            graphs.append(dataset.GRAPHS_NAMES_SHORT[t[0]])
            intel.append(nnz / float(t[1]) / float(4096) * 1e3)
            amd.append(nnz / float(t[2]) / float(4096) * 1e3)
            nvidia.append(nnz / float(t[3]) / float(4096) * 1e3)

        br1 = list(map(lambda x: group_space * x, range(len(intel))))
        br2 = [x + bar_width + bar_space for x in br1]
        br3 = [x + bar_width + bar_space for x in br2]

        plt.style.use(style)
        plt.figure(figsize=fig_size, tight_layout=True)

        plt.bar(br1, intel, width=bar_width, label='Intel Arc a770\n4096 cores')
        plt.bar(br2, amd, width=bar_width, label='AMD Vega FE\n4096 cores')
        plt.bar(br3, nvidia, width=bar_width, label='Nvidia Gtx 1070\n1920 cores')

        plt.xlabel('Graph', fontweight='bold', fontsize=font_size)
        plt.ylabel('Edge throughput per GPU core', fontweight='bold', fontsize=font_size)
        plt.xticks(list(map(lambda x: group_space * x + bar_width + bar_space, range(len(intel)))), graphs,
                   fontsize=font_size * 0.8, rotation=20)
        plt.yscale('log')

        plt.legend()
        plt.savefig(f"rq2_cores_{algo}.pdf", format="pdf")


plot_cpu_gpu_performance("nvidia_all.csv", style='bmh')
plot_gpu_n_core_performance("portability_all.csv", style='bmh')
