#ifndef PROCESS_STATS_H
#define PROCESS_STATS_H

struct ProcessStats : public Statable
{
	StatObj<W64> cycles;
	StatObj<W64> insns;
	StatObj<W64> schedules;

	ProcessStats(const char *name, Statable *parent)
		: Statable(name, parent)
		  , cycles("cycles", this)
		  , insns("insns", this)
		  , schedules("schedules", this)
	{ }
};

#endif
