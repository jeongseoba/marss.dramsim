#ifndef PROCESS_STATS_H
#define PROCESS_STATS_H

struct ProcessStats : public Statable
{
	struct cache : public Statable
	{
		struct hit : public Statable
		{
			struct hit_sub : public Statable
			{
				StatObj<W64> hit;
				StatObj<W64> forward;

				hit_sub(const char *name, Statable *parent)
					: Statable(name, parent)
					  , hit("hit", this)
					  , forward("forward", this)
				{}
			};

			hit_sub read;
			hit_sub write;

			hit(Statable *parent)
				: Statable("hit", parent)
				  , read("read", this)
				  , write("write", this)
			{}
		} hit;

		struct miss : public Statable
		{
			struct miss_sub : public Statable
			{
				StatObj<W64> inst;
				StatObj<W64> data;

				miss_sub(const char *name, Statable *parent)
					: Statable(name, parent)
					  , inst("inst", this)
					  , data("data", this)
				{}
			};

			miss_sub read;
			miss_sub write;

			miss(Statable *parent)
				: Statable("miss", parent)
				  , read("read", this)
				  , write("write", this)
			{}
		} miss;

		cache(Statable *parent)
			: Statable("cache", parent)
			  , hit(this)
			  , miss(this)
		{}
	} cache;

	StatObj<W64> cycles;
	StatObj<W64> insns;
	StatObj<W64> schedules;

	ProcessStats(const char *name, Statable *parent)
		: Statable(name, parent)
		  , cache(this)
		  , cycles("cycles", this)
		  , insns("insns", this)
		  , schedules("schedules", this)
	{ }
};

#endif
